from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .newform import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # if request is post, v create form instance of UsercreatonFrom and this new form has the posted data.
        # later v replace it RegisterForm created in newform.py to include extra fields.
        form = RegisterForm(request.POST)
        # next checks whether form is valid
        if form.is_valid():
            # save the form to db,
            form.save()
            # if valid grab the posted username from the form.
            # form.cleaned_data is a dictionary which contains validated datas
            username = form.cleaned_data.get('username')
            # display a flash messages if success,
            messages.success(request, f'Account Created for {username}')
            # redirect to a login page once submited. here login is name of the urlpattern that renders login page.
            return redirect('login')

    else:
        # if not post request, create an instance of form
        form = RegisterForm()
    # render the templates and pass the form as key value pair. thus v can acces it with in tht template
    return render(request, 'userapp/register.html', {'form': form})


# home view
def home(request):
    return render(request, 'userapp/home.html')

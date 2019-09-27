from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        # if request is post, v create form instance of UsercreatonFrom and this new form has the posted data.
        form = UserCreationForm(request.POST)
        # next checks whether form is valid
        if form.is_valid():
            # if valid grab the posted username from the form.
            form.save()
            # form.cleaned_data is a dictionary which contains validated datas
            username = form.cleaned_data.get('username')
            # display a flash messages if success,
            messages.success(request, f'Account Created for {username}')
            # redirect to a new page once submited. here home is name of the urlpattern that renders home page.
            return redirect('home')
    else:
        # if not post request, create an instance of form
        form = UserCreationForm()
    # render the templates and pass the form as key value pair. thus v can acces it with in tht template
    return render(request, 'userapp/register.html', {'form1': form})


# home view
def home(request):
    return render(request, 'userapp/home.html')

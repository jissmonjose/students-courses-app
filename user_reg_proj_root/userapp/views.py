from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from .newform import RegisterForm
from django.forms import ModelForm
from .models import Contact
from studentapp.models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
@login_required
def home(request):
    return render(request, 'userapp/home.html')


# index view
def index_page(request):
    return render(request, 'userapp/index.html')


# about view
def about_page(request):
    return render(request, 'userapp/about.html')


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


# contact view

def contact(request, template_name='userapp/contact.html'):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        contact_form.save()
        return redirect('index_page')
    return render(request, template_name, {'contact_form': contact_form})


# view students
@login_required
def view_students(request, template_name='userapp/students.html'):
    students_data = Student.objects.order_by('name')

    # students_search filter
    query = request.GET.get("q")
    if query:
        students_data = students_data.filter(
            Q(name__icontains=query) |
            Q(select_course__name__icontains=query) |
            Q(select_batch__batch_number__icontains=query)
        ).distinct()

    paginator = Paginator(students_data, 8)
    page = request.GET.get('page')
    students_page = paginator.get_page(page)

    context = {

        'students_data': students_page
    }
    return render(request, template_name, context)


# each students
def each_student_details(request, stud_id, template_name='userapp/each_stud_details.html'):
    stud = get_object_or_404(Student, pk=stud_id)
    context = {
        'stud': stud
    }
    return render(request, template_name, context)

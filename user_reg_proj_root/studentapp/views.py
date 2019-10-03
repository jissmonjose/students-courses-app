from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Student
from courseapp.models import CourseModel
from django.core.paginator import Paginator


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


# Create your views here.

def student_register(request, template_name='studentapp/apply.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_register')
    return render(request, template_name, {'form': form})


def course_view(request, template_name='studentapp/courses.html'):
    courses = CourseModel.objects.order_by('name')
    paginator = Paginator(courses, 3)
    page = request.GET.get('page')
    page_courses = paginator.get_page(page)

    context = {
        'courses': page_courses
    }

    return render(request, template_name, context)


def each_course(request, template_name='studentapp/'):
    pass


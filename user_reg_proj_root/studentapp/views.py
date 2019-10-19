from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms
from .models import Student
from django.contrib import messages
from courseapp.models import CourseModel
from django.core.paginator import Paginator
from django.core.validators import validate_email


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


# validations

def clean_phone(self, *args, **kwargs):
    phone = self.cleaned_data.get('phone')
    if len(phone) > 8:
        raise forms.ValidationError('not a valid number')
    # Create your views here.


def student_register(request, template_name='studentapp/apply.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        name = form.cleaned_data.get('name')
        course = form.cleaned_data.get('select_course')
        messages.success(request, f'{name} successfully applied for the course {course}')
        return redirect('studentapp:student_register')
    else:
        form = StudentForm()
    return render(request, template_name, {'form': form})


def course_view(request, template_name='studentapp/courses.html'):
    courses = CourseModel.objects.order_by('name')
    # search feature
    query = request.GET.get("q")
    if query:
        courses = courses.filter(name__icontains=query)

    paginator = Paginator(courses, 3)
    page = request.GET.get('page')
    page_courses = paginator.get_page(page)

    context = {
        'courses': page_courses
    }

    return render(request, template_name, context)


# view for each courses
def each_course(request, course_id, template_name='studentapp/each_course.html'):
    course = get_object_or_404(CourseModel, pk=course_id)
    return render(request, template_name, {'course': course})

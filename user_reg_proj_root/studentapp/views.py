from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Student


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

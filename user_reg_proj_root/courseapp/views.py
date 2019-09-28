from django.shortcuts import render
from .course_form import CourseForm
from django.shortcuts import redirect, get_object_or_404
from .models import CourseModel


# Create your views here.
def course_create(request, template_name='courseapp/course.html'):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_create')
    return render(request, template_name, {'form': form})


def course_read(request, pk, template_name='courseapp/courselist.html'):
    course = get_object_or_404(CourseModel, pk=pk)
    return render(request, template_name, {'course': course})

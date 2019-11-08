from django.shortcuts import render
from .course_form import CourseForm
from django.shortcuts import redirect, get_object_or_404
from .models import CourseModel
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def course_create(request, template_name='courseapp/course.html'):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cousrse successfully creatad')
        return redirect('course_create')
    return render(request, template_name, {'form': form})


# course list
@login_required
def course_list(request, template_name='courseapp/courselist.html'):
    courses = CourseModel.objects.all().order_by('name')
    return render(request, template_name, {'course': courses})


# each courses
@login_required
def each_courses(request, pk, template_name='courseapp/course_details.html'):
    each_one = CourseModel.objects.get(pk=pk)
    return render(request, template_name, {'each_one': each_one})


# delete a course
class CourseDelete(LoginRequiredMixin, DeleteView):
    model = CourseModel
    success_url = reverse_lazy('course_list')


# update a course
class CourseEdit(LoginRequiredMixin, UpdateView):
    model = CourseModel
    fields = '__all__'
    success_url = reverse_lazy('course_list')


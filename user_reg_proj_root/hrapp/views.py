from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .hrforms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import TimeTable
from django.contrib.auth.decorators import login_required
from .hrforms import TimeTableForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('hrapp:login')
    else:
        form = RegisterForm()
    return render(request, 'hrapp/register.html', {'form': form})


@login_required
def home(request, template_name='hrapp/home.html'):
    return render(request, template_name)


class TimeTableView(LoginRequiredMixin, CreateView):
    model = TimeTable
    form_class = TimeTableForm
    success_url = reverse_lazy('hrapp:schedule_list')


class TimeTableList(LoginRequiredMixin, ListView):
    model = TimeTable
    context_object_name = 'schedules'

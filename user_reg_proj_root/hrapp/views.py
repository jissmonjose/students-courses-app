from django.shortcuts import render, redirect
from .hrforms import RegisterForm
from django.contrib import messages


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



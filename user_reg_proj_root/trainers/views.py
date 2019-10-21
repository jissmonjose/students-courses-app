from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import TrainerModel
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, DetailView, ListView
from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# create a model form
class TrainerForm(ModelForm):
    class Meta:
        model = TrainerModel
        fields = ['name', 'email', 'phone', 'experience', 'photo']


# Create your views here.

# create trainer
@login_required
def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'asdahdsasl')
            return redirect('trainer_view')
    else:
        form = TrainerForm()
    return render(request, 'trainers/index.html', {'form': form})


# # view all trainer
# def trainer_view(request, template_name='trainers/trainers.html'):
#     data = TrainerModel.objects.all().order_by('name')
#     context = {
#         'data': data
#     }
#     return render(request, template_name, context)


class TrainersList(ListView):
    model = TrainerModel
    context_object_name = 'data'
    template_name = 'trainers/trainers.html'
    ordering = ['-name']


# view each trainer details
# def trainer_one(request, trainer_id, template_name='trainers/each_trainer.html'):
#     new = get_object_or_404(TrainerModel, pk=trainer_id)
#     context = {'new': new}
#     return render(request, template_name, context)
#

class TrainerDetail(DetailView):
    model = TrainerModel
    template_name = 'trainers/each_trainer.html'
    context_object_name = 'new'


# remove trainer
class TrainerDelete(DeleteView):
    model = TrainerModel
    success_url = reverse_lazy('trainer_view')


# edit a trainer
class TrainerEdit(UpdateView):
    model = TrainerModel
    fields = ('name', 'email', 'phone', 'experience')

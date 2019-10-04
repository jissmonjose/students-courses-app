from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import TrainerModel


# create a model form
class TrainerForm(ModelForm):
    class Meta:
        model = TrainerModel
        fields = '__all__'


# Create your views here.

# create trainer
def trainer_create(request):
    form = TrainerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('trainer_view')
    return render(request, 'trainers/index.html', {'form': form})


# view all trainer
def trainer_view(request, template_name='trainers/trainers.html'):
    data = TrainerModel.objects.all().order_by('name')
    context = {
        'data': data
    }
    return render(request, template_name, context)


# view each trainer details
def trainer_one(request, trainer_id, template_name='trainers/each_trainer.html'):
    new = get_object_or_404(TrainerModel, pk=trainer_id)
    context = {'new': new}
    return render(request, template_name, context)

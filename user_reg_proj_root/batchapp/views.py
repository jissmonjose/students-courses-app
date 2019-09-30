from django.shortcuts import render, redirect
from django.forms import ModelForm

from .models import Batch


# Create your views here.

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'


def batch(request, template_name='batchapp/give_batch.html'):
    form = BatchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('batch')
    return render(request, template_name, {'form': form})



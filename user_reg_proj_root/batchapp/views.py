from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib import messages
from .models import Batch


# Create your views here.

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'


# create batch
def batch(request, template_name='batchapp/give_batch.html'):
    form = BatchForm(request.POST or None)
    if form.is_valid():
        form.save()
        num = form.cleaned_data.get('batch_number')
        messages.success(request, f'{num} batch created successfully')
        return redirect('batch')
    return render(request, template_name, {'form': form})


# list batches
def batch_list(request, template_name='batchapp/batches.html'):
    batches = Batch.objects.all()
    return render(request, template_name, {'batch': batches})


# each courses
def each_batch(request, pk, template_name='batchapp/batch_details.html'):
    each_bch = Batch.objects.get(pk=pk)
    return render(request, template_name, {'each_bch': each_bch})


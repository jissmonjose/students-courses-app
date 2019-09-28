from .models import CourseModel
from django.forms import ModelForm


class CourseForm(ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'


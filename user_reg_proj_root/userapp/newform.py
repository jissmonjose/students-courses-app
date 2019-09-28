from django.contrib.auth.forms import UserCreationForm
from django import forms
# import user model
from django.contrib.auth.models import User


# create form
class RegisterForm(UserCreationForm):
    # add fields for the form
    email = forms.EmailField(required=True)

    # Specify Meta class to configure the form with the user model.
    class Meta:
        # specify the model to interact with this new form.
        model = User
        # specify the field to be shown in the form
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
    # validación email
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exist():
            raise forms.ValidationError("Este email está registrado actualmente")
        if len(email) > 350:
            raise forms.ValidationError('tu email supera el límite de texto')
        return email

#login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# update Form
class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta :
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
   

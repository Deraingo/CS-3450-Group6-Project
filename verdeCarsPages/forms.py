from django import forms
from .models import User, Car

class UserForm(forms.ModelForm):
    create_user = forms.BooleanField(initial=True)
    class Meta:
        model = User
        fields = ['fname', 'lname', 'usernm', 'passwd']
        exclude = ['userType', 'money']  # These have default values and are not entered when creating an account

class LoginForm(forms.Form):
    enter_login = forms.BooleanField(initial=True)

    class Meta:
        fields = ['LoginUsername', 'LoginPassword']
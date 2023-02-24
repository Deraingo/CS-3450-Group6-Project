from django import forms
from .models import User, Car

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'usernm', 'passwd']
        exclude = ['userType', 'money']
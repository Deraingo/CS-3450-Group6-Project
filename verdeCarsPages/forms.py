from django import forms
from .models import User, Car
class UserForm(forms.ModelForm):
    create_user = forms.BooleanField(initial=True)
    class Meta:
        model = User
        fields = ['fname', 'lname', 'phoneNumber', 'usernm', 'passwd']
        exclude = ['userType', 'money']  # These have default values and are not entered when creating an account

class LoginForm(forms.ModelForm):
    login_user = forms.BooleanField(initial=True)
    class Meta:
        model = User
        fields = ['usernm', 'passwd']
        exclude = ['fname', 'lname', 'userType', 'money']

class UpdateStranded(forms.Form):
    update_stranded = forms.BooleanField(initial=True)

class ClockHours(forms.ModelForm):
    class Meta:
        model = User
        fields = ['hoursWorked']
        exclude = ['fname', 'lname', 'phoneNumber', 'userType', 'money', 'checkoutCode', 'usernm', 'passwd']


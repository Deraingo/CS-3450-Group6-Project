from django import forms
from .models import User
class UserForm(forms.ModelForm):
    create_user = forms.BooleanField(initial=True)
    class Meta:
        model = User
        fields = ['fname', 'lname', 'phoneNumber', 'usernm', 'passwd']
        exclude = ['userType', 'money']  # These have default values and are not entered when creating an account

# class LoginForm(forms.Form):
#     # enter_login = forms.BooleanField(initial=True)
#     enter_username = forms.CharField()
#     # enter_username.label = "Username"

#     enter_password = forms.CharField()
#     # enter_password.label = "Password"

#     class Meta:
#         fields = ['LoginUsername', 'LoginPassword']

class LoginForm(forms.ModelForm):
    login_user = forms.BooleanField(initial=True)
    class Meta:
        model = User
        fields = ['usernm', 'passwd']
        exclude = ['fname', 'lname', 'userType', 'money']


class UpdateStranded(forms.Form):
    update_stranded = forms.BooleanField(initial=True)

class ClockHours(forms.Form):
    usernm = forms.CharField()
    passwd = forms.CharField()
    hours = forms.IntegerField()
    
  class RentCarForm(forms.ModelForm):
        #rental_day = forms.DateField()
        #rental_money = forms.FloatField()
        #address = forms.CharField()
        #car_cost=forms.FloatField()
        
        class Meta:
            model = User
            fields = []
            exclude = ['fname', 'lname', 'userType', 'usernm', 'passwd','money']
        
        #def clean_payment_amount(self):
            #data = self.cleaned_data['rental_money']
            #if data < car_cost:
             #   raise ValidationError(_('Not enough'))
                
           # return data
    


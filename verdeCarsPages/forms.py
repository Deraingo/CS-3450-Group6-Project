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

#class RentCarForm(forms.ModelForm):
    #rental_day = forms.DateField()
    #rental_money = forms.FloatField()
    #address = forms.CharField()
    #car_cost=forms.FloatField()
        

#         class Meta:
#             model = User
#             fields = []
#             exclude = ['fname', 'lname', 'userType', 'usernm', 'passwd','money']
        
#         def clean_payment_amount(self):
#             data = self.cleaned_data['rental_money']
#             if data < car_cost:
#                raise ValidationError(_('Not enough'))
                
#             return data


    
    
class RequestRetrieval(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['stranded', 'strandedAddress', 'checkoutCode']
        exclude = ['make', 'model', 'year', 'cost', 'rentalStart', 'rentalEnd', 'imageURL']

#class InputMoney(forms.Form):
#    usernm = forms.CharField()
#    passwd = forms.CharField()
#    money = forms.IntegerField()

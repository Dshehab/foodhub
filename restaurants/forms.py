from django import forms 
from .models import Restaurant 
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
	
class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = '__all__'

		widgets = {
			"publish_date": forms.DateInput(attrs={"type":"date"}),
			"opening_time": forms.TimeInput(attrs={"type":"time"}),
			"closing_time": forms.TimeInput(attrs={"type":"time"}),		

		}
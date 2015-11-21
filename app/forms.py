from django import forms
from django.forms import ModelForm
from app.models import *

class LoginForm(forms.Form):
	usuario =forms.CharField(widget=forms.TextInput())
	password=forms.CharField(widget=forms.PasswordInput(render_value=False))

class RubroForm(ModelForm):
	class Meta:
		model=Rubro
		exclude=[]

class AreaForm(ModelForm):
	class Meta:
		model=Area
		exclude=[]

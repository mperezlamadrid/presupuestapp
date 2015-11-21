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
	name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Nombre la descripcion'}))
	description = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Descripcion del area'}))
	status = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estado del area ej: A o I'}))

	class Meta:
		model=Area
		exclude=[]

class BudgetForm(ModelForm):
	class Meta:
		model=Budget
		exclude=[]

class ParameterForm(ModelForm):
	class Meta:
		model=Parameter
		exclude=[]

class ValueParameterForm(ModelForm):
	class Meta:
		model=ValueParameter
		exclude=[]

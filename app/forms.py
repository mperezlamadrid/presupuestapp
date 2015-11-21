from django import forms
from django.forms import ModelForm
from app.models import *

class LoginForm(forms.Form):
	usuario =forms.CharField(widget=forms.TextInput())
	password=forms.CharField(widget=forms.PasswordInput(render_value=False))

class RubroForm(ModelForm):
	name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Nombre del rubro'}))
	description = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Descripcion del rubro'}))
	budgeted_amount = forms.CharField(label="Monto presupuestado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Monto presupuestado del rubro'}))
	real_amount = forms.CharField(label="Monto real", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Monto real del rubro'}))
	status = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estad del rubro ej: Activo o Inactivo'}))
	area = forms.ModelChoiceField(label="Area", queryset=Area.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model=Rubro
		exclude=[]

class AreaForm(ModelForm):
	name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Nombre la descripcion'}))
	description = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Descripcion del area'}))
	status = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estado del area ej: Activo o Inactivo'}))

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

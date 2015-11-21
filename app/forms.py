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
	name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Nombre la presupuesto'}))
	description = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Descripcion del presupuesto'}))
	status = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estado del presupuesto ej: Activo o Inactivo'}))
	rubro = forms.ModelChoiceField(label="Rubro", queryset=Rubro.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model=Budget
		exclude=[]

class ParameterForm(ModelForm):
	attribute = forms.CharField(label="Atributo", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Atributo del parametro'}))
	description = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Descripcion del parametro'}))
	status_parameter = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estado del parametri ej: A o I'}))

	class Meta:
		model=Parameter
		exclude=[]

class ValueParameterForm(ModelForm):
	value = forms.CharField(label="Valor", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Valor del parametro'}))
	parameter = forms.ModelChoiceField(label="Parametro", queryset=Parameter.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	order = forms.CharField(label="Orden", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Orden del valor parametro'}))
	status_value_parameter = forms.CharField(label="Estado", widget=forms.TextInput(attrs={'class':'form-control',
			 'placeholder':'Estado del valor parametro ej: A o I'}))

	class Meta:
		model=ValueParameter
		exclude=[]

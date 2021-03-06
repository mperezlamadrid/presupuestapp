from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.template.defaulttags import csrf_token
from app.models import *
from app.forms import  LoginForm, RubroForm, AreaForm, BudgetForm, ParameterForm, ValueParameterForm

# Esta seccion es para las vistas de autenticacion
def login_view(request):
    mensaje=""
    if request.user.is_authenticated() :
        return  HttpResponseRedirect('/')
    else:
        if request.method=="POST" :
            form=LoginForm(request.POST)
            if form.is_valid():
			    usuario = form.cleaned_data['usuario']
			    password = form.cleaned_data['password']
			    usuariov = authenticate(username=usuario,password=password)
			    if usuariov is not None and usuariov.is_active:
			        login(request,usuariov)
			        return HttpResponseRedirect('/')
			    else:
			        mensaje ="Usuario y/o Contrasena incorrecta"
        form =LoginForm()
        ctx={'form':form,'mensaje':mensaje}
        return render_to_response('login.html',ctx,RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
# ------------------

def index(request):
    return render_to_response('index.html')


def view_rubros(request):
    return render_to_response('view_rubros.html', {
        'rubros': Rubro.objects.all()
    })

def crear_rubro(request):
    if request.method =="POST":
        form=RubroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/rubros")
    else:
        form=RubroForm()
        return  render_to_response( "crear_rubro.html", {'form':form}, context_instance=RequestContext(request) )

def view_budgets(request):
    return render_to_response('view_budgets.html', {
        'budgets': Budget.objects.all()
    })

def crear_presupuesto(request):
    if request.method =="POST":
        form=BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/rubros")
    else:
        form=BudgetForm()
        return  render_to_response( "crear_presupuesto.html", {'form':form}, context_instance=RequestContext(request) )

def view_areas(request):
    return render_to_response('view_areas.html', {
        'areas': Area.objects.all()
    })

def crear_area(request):
    if request.method =="POST":
        form=AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/areas")
    else:
        form=AreaForm()
        return  render_to_response( "crear_area.html", {'form':form}, context_instance=RequestContext(request) )

def view_parameter(request):
    return render_to_response('view_parameter.html', {
        'parametros': Parameter.objects.all()
    })

def crear_parameter(request):
    if request.method =="POST":
        form=ParameterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/rubros")
    else:
        form=ParameterForm()
        return  render_to_response( "crear_parametro.html", {'form':form}, context_instance=RequestContext(request) )

def view_value_parameter(request):
    return render_to_response('view_value_parameter.html', {
        'valores_parametros': ValueParameter.objects.all()
    })

def crear_value_parameter(request):
    if request.method =="POST":
        form=ValueParameterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/rubros")
    else:
        form=ValueParameterForm()
        return  render_to_response( "crear_valor_parametro.html", {'form':form}, context_instance=RequestContext(request) )

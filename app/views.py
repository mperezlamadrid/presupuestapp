from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from app.models import *

def index(request):
    return render_to_response('index.html')


def view_rubros(request):
    return render_to_response('view_rubros.html', {
        'rubros': Rubro.objects.all()
    })

def view_budgets(request):
    return render_to_response('view_budgets.html', {
        'budgets': Budget.objects.all()
    })

def view_areas(request):
    return render_to_response('view_areas.html', {
        'areas': Area.objects.all()
    })

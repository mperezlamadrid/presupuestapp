"""presupuestapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^rubros/', views.view_rubros),
    url(r'^crear-rubro/$',views.crear_rubro),
    url(r'^presupuestos/', views.view_budgets),
    url(r'^crear-presupuesto/$',views.crear_presupuesto),
    url(r'^areas/', views.view_areas),
    url(r'^crear-area/$',views.crear_area),
    url(r'^parametros/', views.view_parameter),
    url(r'^valor_parametros/', views.view_value_parameter),
    url(r'^login/$',views.login_view,name='vista_login'),
    url(r'^logout/$',views.logout_view,name='vista_logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

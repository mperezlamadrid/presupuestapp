from django.contrib import admin
from app.models import *

class RubroAdmin(admin.ModelAdmin):
    list_display=('id','name','description','budgeted_amount','real_amount', 'status', 'get_area')

class AreaAdmin(admin.ModelAdmin):
    list_display=('id','name','description', 'status')

class BudgetAdmin(admin.ModelAdmin):
    list_display=('id','name','description', 'status', 'rubros', 'total')

class ParameterAdmin(admin.ModelAdmin):
    list_display=('id','attribute','description', 'status_parameter')

class ValueParameterAdmin(admin.ModelAdmin):
    list_display=('id','value','parameter', 'order', 'status_value_parameter')

admin.site.register(Rubro,RubroAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Budget,BudgetAdmin)
admin.site.register(Parameter,ParameterAdmin)
admin.site.register(ValueParameter,ValueParameterAdmin)

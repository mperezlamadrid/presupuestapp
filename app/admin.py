from django.contrib import admin
from app.models import *

class RubroAdmin(admin.ModelAdmin):
    list_display=('id','name','description','budgeted_amount','real_amount', 'status')

class AreaAdmin(admin.ModelAdmin):
    list_display=('id','name','description', 'status')

class BudgetAdmin(admin.ModelAdmin):
    list_display=('id','name','description', 'status', 'rubros', 'total')

admin.site.register(Rubro,RubroAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Budget,BudgetAdmin)

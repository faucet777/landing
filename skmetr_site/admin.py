from django.contrib import admin
from django import forms
from .models import *

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('cat_tag', 'cat_name', 'cat_description')

class UnitsAdmin(admin.ModelAdmin):
    list_display = ('unit_tag', 'unit_name', 'unit_okei')

class ServicesAdminForm(forms.ModelForm):
    serv_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Services
        fields = ('serv_cat', 'serv_tag', 'serv_name', 'serv_description', 'serv_unit', 'serv_unit_price', 'serv_img')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('serv_cat', 'serv_tag', 'serv_name', 'serv_description', 'serv_unit', 'serv_unit_price', 'serv_img')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Units, UnitsAdmin)
admin.site.register(Services, ServicesAdmin)




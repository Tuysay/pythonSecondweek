from django.contrib import admin
from project.models import *

from project.forms import AplicationForm
from project.models import Aplication, User, Category


class AplicationAdmin(admin.ModelAdmin):
    form = AplicationForm
    list_filter = ('status',)
    list_display = ('status', 'name', 'date', 'Category',)
    fields = ('status', 'second_photo', 'comment')



admin.site.register(User)
admin.site.register(Aplication, AplicationAdmin)
admin.site.register(Category)

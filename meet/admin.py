from django.contrib import admin
from django.db import models
from .models import Meet,Location,Participant
# Register your models here.
# admin.site.register(Meet)

class MeetAdmin(admin.ModelAdmin):
    list_display=('title','date','location')
    list_filter=('location','date')
    prepopulated_fields={"slug":('title',)}


admin.site.register(Meet,MeetAdmin)
admin.site.register(Location)
admin.site.register(Participant)

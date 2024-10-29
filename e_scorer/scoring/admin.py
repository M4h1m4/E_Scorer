from django.contrib import admin
from . import  models


# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Judge)
admin.site.register(models.Performer)
admin.site.register(models.Score)
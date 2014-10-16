from django.db import models
from django.contrib import admin
# Create your models here.

class Mandu(models.Model):
    seq = models.IntegerField();
    name = models.CharField(max_length=30)
    count  = models.IntegerField()


class ManduAdmin(admin.ModelAdmin):
    list_display = ["name", "count"]
    search_fields = ["name"]


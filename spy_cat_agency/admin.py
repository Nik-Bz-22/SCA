from django.contrib import admin

from spy_cat_agency.models import Cat, Target, Mission

# Register your models here.

admin.site.register(Cat)
admin.site.register(Target)
admin.site.register(Mission)
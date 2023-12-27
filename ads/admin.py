from django.contrib import admin

from .models import Category, Ad, AdImage

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(AdImage)
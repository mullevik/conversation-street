from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Like)

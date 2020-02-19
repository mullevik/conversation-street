"""
Contents:

- Admin helper classes for better forms in administration

- Registration of database models. Every model editable in the administration
    needs to be registered here

"""

from django.contrib import admin

from .models import *

# Enable read-only un-editable fields


class QuestionAdmin(admin.ModelAdmin):
    """Admin helper for showing un-editable information for question"""
    readonly_fields = (
        'identifier',
        'date_created',
        'date_modified',
    )


class CategoryAdmin(admin.ModelAdmin):
    """Admin helper for showing un-editable information for category"""
    readonly_fields = (
        'identifier',
        'date_created',
    )


class TagAdmin(admin.ModelAdmin):
    """Admin helper for showing un-editable information for tag"""
    readonly_fields = (
        'identifier',
        'date_created',
    )


# Register your models here.
admin.site.register(Profile)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Like)

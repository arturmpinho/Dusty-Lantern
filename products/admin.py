from django.contrib import admin
from .models import Category, Condition, Product, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'fa_icon_class'
    )


class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_description',
    )


class ImageAdmin(admin.TabularInline):

    model = Image

    list_display = (
        'id',
        'image',
        'main_image',
        'product',
    )


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    list_display = (
        'id',
        'title',
        'category',
        'condition',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Product, ProductAdmin)

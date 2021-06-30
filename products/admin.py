from django.contrib import admin
from .models import Category, Condition, Product, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )


class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_description',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'username',
        'category',
        'condition',
    )


class ImageAdmin(admin.ModelAdmin):

    def get_product(self, obj):
        """ Function to display attribute from ForeignKey """
        return obj.product.id, obj.product.username, obj.product.title

    get_product.admin = 'product_id',

    list_display = (
        'id',
        'image',
        'main_image',
        'product',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)

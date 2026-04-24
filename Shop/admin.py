from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
     def __str__(self):
        return self.name
    
     list_display = ('name', 'price')
     search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

    list_display = ('name',)
    search_fields = ('name',)
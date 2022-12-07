from django.contrib import admin
from .models import PrimaryCategoryModel, SecondaryCategoryModel, ProductModel



class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(PrimaryCategoryModel)
admin.site.register(SecondaryCategoryModel)
admin.site.register(ProductModel, ProductModelAdmin)


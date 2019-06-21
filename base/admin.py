from django.contrib import admin
from base.models import Member, Product, ProductType


class MemberAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

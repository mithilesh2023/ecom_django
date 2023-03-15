from django.contrib import admin
from shop.models import *
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    search_fields=["id","title"]
    def delete_button(self,obj):
        return format_html("<a href='/admin/shop/category/{}/delete'>Delete</a>",obj.id)

    def update_button(self,obj):
        return format_html("<a href='/admin/shop/category/{}/change'>Edit</a>",obj.id)

    list_display=["id","title","description","slug",'delete_button','update_button']
    list_display_links=['title','slug']
    prepopulated_fields={"slug":("title",)}

class ProductAdmin(admin.ModelAdmin):
     search_fields=["id","name"]
     def delete_button(self,obj):
        return format_html("<a href='/admin/shop/category/{}/delete'>Delete</a>",obj.id)

     def update_button(self,obj):
        return format_html("<a href='/admin/shop/category/{}/change'>Edit</a>",obj.id)

     list_display=["id","name","description","slug",'delete_button','update_button']
     list_display_links=['name','slug']
     prepopulated_fields={"slug":("name",)}

admin.site.register (Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Student)

class orderi(admin.ModelAdmin):
     list_display=["id","item",]

admin.site.register(OrderItem,orderi)
admin.site.register(Order)
class cou(admin.ModelAdmin):
     search_fields=["id","coupon"]
     

     list_display=["id","code","amount"]
     

admin.site.register(Coupon,cou)
admin.site.register(Address)
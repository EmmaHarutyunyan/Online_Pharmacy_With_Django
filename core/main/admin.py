from django.contrib import admin
from . models import Slide,Home_products,Product,About,ContactUs,CartItem

# Register your models here.

admin.site.register(Slide)
admin.site.register(Home_products)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(CartItem)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    search_fields = ['fname','lname']
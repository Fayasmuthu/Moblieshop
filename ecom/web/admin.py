from django.contrib import admin
from .models import Product , Members ,Teamoffer ,LatestA ,LatestB,Order,Orderitem

# Register your models here.

class OrderitemTubleInline(admin.TabularInline):
    model=Orderitem
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderitemTubleInline]

admin.site.register(Product),
admin.site.register(Members),
admin.site.register(Teamoffer),
admin.site.register(LatestA),
admin.site.register(LatestB),
admin.site.register(Order,OrderAdmin),
admin.site.register(Orderitem)
from django.contrib import admin
from .models import Product , Members ,Teamoffer ,LatestA ,LatestB,Order,Orderitem, Email,Contact,Leave_message

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
admin.site.register(Orderitem),
admin.site.register(Email),
admin.site.register(Contact),
admin.site.register(Leave_message)

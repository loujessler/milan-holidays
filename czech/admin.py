from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    list_display = ["time_from","time_return_transfer","name","id","status","created","updated"]
    # list_display = [field.name for field in Order._meta.fields]
    # fields = ["from_transfer", "time_from", "to_transfer", "passenger", "children", "time_return_transfer", "children_passenger", "email", "comments"]
    list_filter = ("time_from",'status', 'updated')
    search_fields = ['name','id',"time_from"]

    class Meta:
        model = Order

# admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Car)
admin.site.register(Drivers)
admin.site.register(Status)
admin.site.register(StatusPay)
admin.site.register(Questions)
# admin.site.register(MyModel)
# Register your models here.

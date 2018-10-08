from django.contrib import admin
from .models import Branch
from .models import Locomotive
from .models import Period

class ViewColombsLocomotive(admin.ModelAdmin):
    list_display = ['name', 'rate']
    list_display_links = ['name', 'rate']
    # list_filter = ['create_date', 'balance']
    # search_fields = ['name', 'fname']
    class Meta():
        model = Locomotive
#
class ViewColombsPeriod(admin.ModelAdmin):
    list_display = ['year', 'locomotive', 'branch', 'run']
    list_display_links = ['year', 'branch', 'run']
#     list_filter = ['region', 'sity']
#     # search_fields = ['name', 'fname']
    class Meta():
        model = Period
#
#
# class ViewColombsContact(admin.ModelAdmin):
#     list_display = ['worker', 'type_contact', 'contact']
#     list_display_links = ['worker', 'type_contact', 'contact']
#     list_filter = ['type_contact']
#     # search_fields = ['name', 'fname']
#     class Meta():
#         model = Contact

admin.site.register(Branch)
admin.site.register(Locomotive, ViewColombsLocomotive)
admin.site.register(Period, ViewColombsPeriod)
# admin.site.register(Contact, ViewColombsContact)
# admin.site.register(Adress, ViewColombsAdress)



# admin.site.register(Worker)



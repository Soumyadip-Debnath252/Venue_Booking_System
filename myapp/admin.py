from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser, Venue, Book
# Register your models h
admin.site.site_header  =  "Venue Booking Administration"
admin.site.site_title  =  "Administration"
admin.site.index_title  =  "Venue Booking"

admin.site.unregister(Group)

@admin.register(Venue)
class VenueFormAdmin(admin.ModelAdmin):
    list_display=('vname', 'vdescriptions', 'vtype','vaddress','vcharges')


# @admin.register(CustomUser)
# class VenueFormAdmin(admin.ModelAdmin):
#     list_display=('first_name', 'last_name', 'email','mobile','address')

@admin.register(Book)
class BookingFormAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['']
    list_display = ('bookby','name','description','bookdate', 'eventdate' )

    def bookby(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
        
    def name(self, obj):
        return obj.venue.vname

    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

from django.contrib import admin
from .models import Plot, PlotOccupant, PlotPic

# Register your models here.
class PlotAdmin(admin.ModelAdmin):
    list_display = ['plot_number', 'plot_price', 'plot_address', 'plot_rating']
    list_filter = ['plot_bedsitter', 'plot_1B', 'plot_2B', 'plot_3B']

admin.site.register(Plot, PlotAdmin)

class PlotPicAdmin(admin.ModelAdmin):
    list_display = ['plot_number', 'plot_pic', 'plot_pic_desc']
    search_fields = ['plot_number', 'plot_pic_desc']

admin.site.register(PlotPic, PlotPicAdmin)

class PlotOccupantAdmin(admin.ModelAdmin):
    list_display = ['plot_number', 'plot_occupant_f_name', 'plot_occupant_l_name', 'plot_occupant_class', 'plot_occupant_phone', 'plot_occupant_email']
    search_fields = ['plot_number', 'plot_occupant_f_name', 'plot_occupant_l_name']
    list_filter = ['plot_occupant_class']

admin.site.register(PlotOccupant, PlotOccupantAdmin)
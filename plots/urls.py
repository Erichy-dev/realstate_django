from django.urls import path

from . import views

urlpatterns = [
  path('', views.get_plots, name='plots'),
  path("plot/<str:plot_number>/", views.get_plot, name="plot"),
  path("<str:plot_number>/pics/", views.get_plot_pics, name="plot_pics"),
  path("create_plot_pics/", views.create_plot_pics, name="create_plot_pics"),
  path("<str:plot_number>/caretakers/", views.get_plot_caretakers, name="plot_caretakers"),
  path("create_occupant/", views.create_plot_occupant, name="create_plot_occupant"),
]
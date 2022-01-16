from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.matchstat_form, name ="home"),
    path('delete/<int:id>',views.matchstat_del, name= "matchstatsdel"),
    path('<int:id>',views.update_matchstats, name= "matchstatsupdate"),
]
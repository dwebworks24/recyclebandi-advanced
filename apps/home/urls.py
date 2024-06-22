from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('datatables/', views.datatables, name='datatables'),

]

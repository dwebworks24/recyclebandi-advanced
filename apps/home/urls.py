from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('dashboard/', views.cluster_datatables, name='dashboard'),
    path('employee_datatables/', views.datatables, name='employee_datatables'),
    path('cluster_datatables/', views.datatables, name='cluster_datatables'),
    path('addshop/', views.add_shop, name='addshop'),
    path('shop_list/', views.shop_list, name='shop_list'),

]

from django.urls import path, re_path
from apps.home import views
from apps.home import controller_logic

urlpatterns = [   
    path('dashboard/', views.datatables, name='employee_datatables'),
    path('cluster_dashboard/', views.cluster_dashboard, name='cluster-dashboard'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_updated/', controller_logic.password_updated, name='password_updated'),
    # path('upload/', views.upload_file, name='upload_file'),
]

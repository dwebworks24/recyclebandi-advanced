from django.urls import path
from apps.authentication import views

urlpatterns = [
    path('', views.otp_login, name='home'),
    path('sigin/', views.sigin, name='sigin'),
]
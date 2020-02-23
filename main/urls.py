from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='main-home'),
    path('donate/', views.donate, name='main-donate'),
    path('partner/', views.partner, name='main-partner'),
    url(r'^$', views.HomeView.as_view(), name='home')
]
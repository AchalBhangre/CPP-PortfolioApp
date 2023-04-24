from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('portfolio_registration_view', views.portfolio_registration_view, name='portfolio_registration_view'),
    path('signup/', views.signupview, name='signup'),
    path('view_portfolio', views.view_portfolio, name='view_portfolio'),
    path('portfolio_list', views.portfolio_list, name='portfolio_list'),
    path('registrations/<int:registration_id>/', views.registration_details, name='registration_details'),
    path('portfolio_detail/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('about/', views.about, name='about'),
]


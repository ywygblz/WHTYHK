
from django.urls import path

from. import views

app_name = 'django_mako_plus'

urlpatterns = [

    path('index/', views.index, name='index'),

    path('base/', views.base, name='base'),

    path('airline_user/', views.Airline_User.as_view(), name='airline_user')
]
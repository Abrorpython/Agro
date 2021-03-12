from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('razdel/', views.razdel, name="razdel"),
    path('advert/', views.advert, name="advert"),
    path('prodayu/', views.form, name="form"),
    # path('<n>/', views.form, name="form"),
    path('add/', views.add, name="add"),
    path('registr/', views.regist, name="registr"),
    path('customers/',views.customers,name='customers'),
    path('salers/',views.salers,name='salers')
]

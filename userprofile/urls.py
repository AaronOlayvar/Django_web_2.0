from django.urls import path
from . import views

urlpatterns =[
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
]
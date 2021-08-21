from django.urls import path, include
from . import views

urlpatterns = [    
    path('lista-productos/', views.product_list),
    
]

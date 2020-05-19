from django.urls import path
from .views import *

app_name='core'

urlpatterns = [
    path('product/', product, name='product'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customer/', customer, name='customer'),

]

from django.urls import path
from . import views

app_name = 'wagtail_amazon_paapi'

urlpatterns = [
    path('update-product/<int:snippet_id>/', views.update_amazon_product, name='update_amazon_product'),
]

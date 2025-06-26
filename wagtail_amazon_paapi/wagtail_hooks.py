from django.urls import include, path
from wagtail import hooks
from . import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('amazon-api/', include(urls, namespace='wagtail_amazon_paapi')),
    ]


@hooks.register('insert_global_admin_css')
def amazon_product_block_admin_css():
    return '<link rel="stylesheet" href="/static/wagtail_amazon_paapi/css/amazon_product_block_admin.css">'
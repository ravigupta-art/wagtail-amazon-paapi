from django.urls import include, path
from wagtail import hooks
from . import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('amazon-api/', include(urls, namespace='wagtail_amazon_paapi')),
    ]

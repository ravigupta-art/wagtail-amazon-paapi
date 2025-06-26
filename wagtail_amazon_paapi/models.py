from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet 
from wagtail import blocks
from .blocks import AmazonProductSnippetBlock

# Import our new custom panel
from .panels import AmazonUpdatePanel

@register_snippet
class AmazonProductSnippet(models.Model):
    asin = models.CharField(max_length=20, unique=True, help_text="The Amazon Standard Identification Number.")
    product_title = models.CharField(max_length=255, blank=True)
    affiliate_url = models.URLField(max_length=2048, blank=True)
    image_url = models.URLField(max_length=2048, blank=True)
    price = models.CharField(max_length=100, blank=True)

    panels = [
        FieldPanel('asin'),
        AmazonUpdatePanel(),
        # Custom panel for updating product information
        FieldPanel('product_title'),
        FieldPanel('affiliate_url'),
        FieldPanel('image_url'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return self.product_title or self.asin

    class Meta:
        verbose_name_plural = 'Amazon Product Snippets'

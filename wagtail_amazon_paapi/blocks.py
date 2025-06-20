from wagtail.blocks import StructBlock, ChoiceBlock, IntegerBlock
from wagtail.snippets.blocks import SnippetChooserBlock
import uuid

class AmazonProductSnippetBlock(StructBlock):
    """A block for displaying an Amazon Product Snippet with configurable styling."""
    product = SnippetChooserBlock('wagtail_amazon_paapi.AmazonProductSnippet')
    display_style = ChoiceBlock(
        choices=[
            ('simple', 'Simple - Clean minimal design'),
            ('card', 'Card - Boxed layout with shadow'),
            ('horizontal', 'Horizontal - Side-by-side layout'),
        ],
        default='card',
        required=True,
        help_text='Choose how this product should be displayed'
    )
    max_width = IntegerBlock(
        required=False,
        help_text='Maximum width in pixels (leave empty for default sizing)',
        min_value=100,
        max_value=1200
    )
    max_height = IntegerBlock(
        required=False,
        help_text='Maximum height in pixels (leave empty for automatic height)',
        min_value=100,
        max_value=1200
    )

    class Meta:
        template = "wagtail_amazon_paapi/blocks/amazon_product_snippet.html"
        icon = "cart"
        label = "Amazon Product"
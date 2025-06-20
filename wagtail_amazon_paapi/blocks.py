from wagtail.blocks import StructBlock, ChoiceBlock
from wagtail.snippets.blocks import SnippetChooserBlock

class AmazonProductSnippetBlock(StructBlock):
    """A block for displaying an Amazon Product Snippet with selectable style."""
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

    class Meta:
        template = "wagtail_amazon_paapi/blocks/amazon_product_snippet.html"
        icon = "cart"
        label = "Amazon Product"
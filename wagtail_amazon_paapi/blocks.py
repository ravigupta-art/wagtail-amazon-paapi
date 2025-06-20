from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock

class AmazonProductSnippetBlock(blocks.StructBlock):
    """
    A block that allows choosing a pre-configured Amazon Product Snippet.
    """
    product = SnippetChooserBlock('wagtail_amazon_paapi.AmazonProductSnippet')

    class Meta:
        template = 'wagtail_amazon_paapi/blocks/amazon_product_snippet.html'
        icon = 'pick' # A more appropriate icon can be chosen based on your needs
        help_text = 'Select an Amazon Product Snippet to embed.'
        # This label will be used in the Wagtail admin interface
        label = 'Amazon Product Snippet'
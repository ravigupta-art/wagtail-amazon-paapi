from wagtail.blocks import StructBlock, ChoiceBlock, IntegerBlock, CharBlock
from wagtail.snippets.blocks import SnippetChooserBlock

class AmazonProductSnippetBlock(StructBlock):
    """A block for displaying an Amazon Product Snippet with configurable styling."""
    product = SnippetChooserBlock('wagtail_amazon_paapi.AmazonProductSnippet')
    
    # Display style options
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
    
    # Dimension options
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
    
    block_alignment = ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='left',
        required=False,
        help_text='Alignment of the entire block on the page'
    )

    text_alignment = ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='left',
        required=False,
        help_text='Text alignment for the content inside the block'
    )

    background_color = CharBlock(
        required=False,
        help_text='Background color for the block (e.g., #ffffff)',
        max_length=20
    )

    # Font options
    font_family = ChoiceBlock(
        choices=[
            ('inherit', 'Use site default'),
            ('Arial, sans-serif', 'Arial'),
            ('Helvetica, Arial, sans-serif', 'Helvetica'),
            ('Georgia, serif', 'Georgia'),
            ('Tahoma, Geneva, sans-serif', 'Tahoma'),
            ('Trebuchet MS, sans-serif', 'Trebuchet MS'),
            ('Verdana, Geneva, sans-serif', 'Verdana'),
            ('Courier New, monospace', 'Courier New'),
            ('Times New Roman, serif', 'Times New Roman'),
            ('Roboto, sans-serif', 'Roboto (Google)'),
            ('Open Sans, sans-serif', 'Open Sans (Google)'),
            ('Montserrat, sans-serif', 'Montserrat (Google)'),
            ('Lato, sans-serif', 'Lato (Google)'),
            ('Poppins, sans-serif', 'Poppins (Google)'),
        ],
        default='inherit',
        required=True,
        help_text='Select font family for product display'
    )
    
    # Typography options
    title_size = ChoiceBlock(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium (Default)'),
            ('large', 'Large'),
        ],
        default='medium',
        required=False,
        help_text='Title font size'
    )
    
    title_weight = ChoiceBlock(
        choices=[
            ('normal', 'Normal'),
            ('bold', 'Bold (Default)'),
        ],
        default='bold',
        required=False,
        help_text='Title font weight'
    )
    
    title_color = CharBlock(
        required=False,
        help_text='Title text color (e.g., #333333 or darkblue)',
        max_length=20
    )
    
    price_size = ChoiceBlock(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium (Default)'),
            ('large', 'Large'),
        ],
        default='medium',
        required=False,
        help_text='Price font size'
    )

    price_weight = ChoiceBlock(
        choices=[
            ('normal', 'Normal'),
            ('bold', 'Bold (Default)'),
        ],
        default='bold',
        required=False,
        help_text='Price font weight'
    )

    price_color = CharBlock(
        required=False,
        help_text='Price text color (e.g., #009900 or darkgreen)',
        max_length=20
    )



    button_text = CharBlock(
        required=False,
        help_text='Custom button text (default: "Buy on Amazon")',
        max_length=30,
        default='Buy on Amazon'
    )

    button_size = ChoiceBlock(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium (Default)'),
            ('large', 'Large'),
        ],
        default='medium',
        required=False,
        help_text='Button padding size'
    )

    button_text_size = ChoiceBlock(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium (Default)'),
            ('large', 'Large'),
        ],
        default='medium',
        required=False,
        help_text='Font size for button text'
    )

    button_text_weight = ChoiceBlock(
        choices=[
            ('400', 'Normal'),
            ('500', 'Medium'),
            ('600', 'Semi-bold (Default)'),
            ('700', 'Bold'),
        ],
        default='600',
        required=False,
        help_text="Button text weight."
    )
    
    button_text_color = CharBlock(
        required=False,
        help_text='Button text color',
        max_length=20
    )

    button_style = ChoiceBlock(
        choices=[
            ('rounded', 'Rounded Rectangle'),
            ('pill', 'Pill'),
            ('rectangle', 'Rectangle'),
        ],
        default='rounded',
        required=False,
        help_text='Button shape style'
    )

    button_color = CharBlock(
        required=False,
        help_text='Button background color (e.g., #ff9900 or orange)',
        max_length=20,
        default='#ff9900'
    )

    button_corner_radius = IntegerBlock(
        required=False,
        help_text='Corner radius when using rounded style',
        min_value=0,
        max_value=50,
        default=4
    )

    class Meta:
        template = "wagtail_amazon_paapi/blocks/amazon_product_snippet.html"
        icon = "snippet"
        label = "Amazon Product"
        form_classname = "amazon-product-block-form struct-block"
        form_template = "wagtail_amazon_paapi/blocks/amazon_product_snippet_form.html"


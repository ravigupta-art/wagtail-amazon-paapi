# wagtail-amazon-paapi
##### Wagtail Amazon PA-API Integration
This package provides integration between Wagtail CMS and Amazon's Product Advertising API (PA-API), allowing you to display Amazon products on your Wagtail site with affiliate links.

Note: This project is not affiliated with or endorsed by Amazon. Use of the AWS Product Advertising API is subject to Amazon Associates Program Policies. 

## Features

- Store Amazon product data as snippets in Wagtail
- Fetch product details directly from Amazon's PA-API
- Display products with customizable styling in your Wagtail pages
- Update product information with a single click

## Installation

> ⚠️ **Note:** This package is not yet available on PyPI due to pending verification of the Amazon API integration. For now, you must install from the local source.

### Local Installation

Clone the repository and install it locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/wagtail-amazon-paapi.git
cd wagtail-amazon-paapi

# Install in development mode
pip install -e .
```

Or install directly from your local copy:

```bash
pip install -e /path/to/wagtail-amazon-paapi
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'wagtail_amazon_paapi',
    # ...
]
```

## Configuration

Add your Amazon PA-API credentials to your Django settings:

```python
# Amazon PA-API credentials
WAGTAIL_AMAZON_PRODUCTS = {
    'AMAZON_PAAPI_ACCESS_KEY': 'YOUR_ACCESS_KEY',  # Use environment variables for security
    'AMAZON_PAAPI_SECRET_KEY': 'YOUR_SECRET_KEY',  # Use environment variables for security
    'AMAZON_PAAPI_PARTNER_TAG': 'your-associate-tag',  # Your tracking ID
    'AMAZON_PAAPI_COUNTRY': 'US',  # Country code for the Amazon marketplace
}
```

Set DEFAULT_AUTO_FIELD to 'django.db.models.BigAutoField' in Django settings:

```python
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

In your page model, import and use the AmazonProductSnippetBlock to incorporate the snippet into a StreamField:

```python
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail_amazon_paapi.blocks import AmazonProductSnippetBlock

class ExamplePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('amazon_product', AmazonProductSnippetBlock()),
        # other blocks...
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```


Run makemigrations:

```bash
python manage.py makemigrations
```

Run migrate:

```bash
python manage.py migrate
```

## Usage

### Creating Product Snippets

1. **In the Wagtail admin**, go to **Snippets** → **Amazon Product Snippets**.  
2. **Click "Add Amazon Product Snippet"**.  
3. **Enter the ASIN**
   - Add other details manually.
   - You can get affliate url using SiteSrtrip feature in you affliate account.
   - product image can be retrieved by getting a image URL from product page.
   - Right now adding this information manually is important. This part will keep working even when you loose PA-API access. Refer this doc:https://webservices.amazon.com/paapi5/documentation/troubleshooting/api-rates.html
4. **Click "Save"**. Once saved, you should see an **"Update from Amazon API"** button (provided by the custom panel in `AmazonUpdatePanel`). Clicking it will fetch fresh data (title, price, image, etc.) from Amazon and fill in the snippet fields.

### Using the StreamField Block

In your page model, import and use the `AmazonProductSnippetBlock` to incorporate the snippet into a `StreamField`:

```python
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail_amazon_paapi.blocks import AmazonProductSnippetBlock

class ExamplePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('amazon_product', AmazonProductSnippetBlock()),
        # other blocks...
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

Now, in the Wagtail admin **Pages** section, when editing/creating an `ExamplePage`, you can select **Amazon Product** from the StreamField block chooser. This lets you pick a snippet you previously created in **Snippets** → **Amazon Product Snippets**.

### Updating Product Information

Over time, product details (like price) can change. To keep your snippet data up to date:

1. Go to **Snippets** → **Amazon Product Snippets**.  
2. Select the product snippet you want to refresh.  
3. Click **"Update from Amazon API"**.  
4. Status messages (success/failure) will appear to reflect the update result.  

## Customizing the Panel Template

By default, `amazon_update_panel.html` contains a button labeled **"Update From Amazon API"**. This button fetches the ASIN data from Amazon whenever clicked. If you wish to customize the look, text, or layout, edit the template

---

## Customizing the Product Template

How an Amazon product snippet is displayed on your site is controlled by `amazon_product_snippet.html`. You can override this template in your own `templates` directory if you want a different design. 

---

## Customization Options

When adding Amazon product blocks to your pages, you can fully customize their appearance:

### Display Styles

Choose from three layout styles:
- **Simple** - Clean minimal design
- **Card** - Boxed layout with shadow
- **Horizontal** - Side-by-side layout

### Size Controls

Set exact dimensions to fit your design:
- **Max Width** - Control the width in pixels
- **Max Height** - Limit height with automatic overflow

### Typography Options

Fully customize text appearance:
- **Font Family** - Choose from web-safe fonts or Google Fonts
- **Title Size** - Small, medium, or large options
- **Title Weight** - Normal or bold
- **Title Color** - Custom color for the product title
- **Price Color** - Custom color for the price display
- **Button Text** - Customize the call-to-action text
- **Block Alignment** - Left, center or right alignment of the entire card
- **Text Alignment** - Align text left, center or right within the card
- **Background Color** - Custom background color for the ad card
- **Price Size** - Control the price font size
- **Price Weight** - Normal or bold weight for the price text

![Amazon Product Edit Interface](docs/images/screenshot_01.png)
*Screenshot: Configuring an Amazon product block in the Wagtail admin*

![Amazon Product Display](docs/images/screenshot_02.png)
*Screenshot: Example of Amazon product blocks with different styles*

## Current Limitations

**Package Status:**
> ⚠️ **Important:** This package is currently in development and not available on PyPI. The primary reason is that the automatic product updates feature has an issue with Amazon API rate limits. Manual entry of product details is fully functional and demonstrated in this package. The automatic update functionality needs further verification before public release. This will be addressed in a future update, or contributions to verify this functionality are welcome.

## Extending

You can override the default templates by creating your own versions at:
- `templates/wagtail_amazon_paapi/blocks/amazon_product_snippet.html`
- `templates/wagtail_amazon_paapi/admin/panels/amazon_update_panel.html`

## License

This project is licensed under the MIT License.

## Credits and License

- **Author**: [Ravi Gupta](mailto:ravi.opensource@protonmail.com)  
- **License**: [MIT](https://opensource.org/licenses/MIT)  

This project is not affiliated with or endorsed by Amazon. Use of the AWS Product Advertising API is subject to Amazon Associates Program Policies. 

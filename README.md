```
This Project is regarding a wagtail project that will help users to add amazon products to snippets and those snippets to pages to advertise on their blogs/websites.
```
# Wagtail Amazon PA-API Integration

A **Wagtail** application that integrates with the **Amazon Product Advertising API (PA-API)**, allowing you to easily manage Amazon products in your Wagtail site and embed them into any page. This package consists of:

1. A **snippet model** for storing product data (`AmazonProductSnippet`)  
2. A **custom block** (`AmazonProductSnippetBlock`) for embedding these products into a `StreamField`  
3. **Admin panels** and **views** that allow you to fetch or update product data from Amazon with a single click  

Table of Contents:
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
  - [Creating Product Snippets](#creating-product-snippets)  
  - [Using the StreamField Block](#using-the-streamfield-block)  
  - [Updating Product Information](#updating-product-information)  
- [Customizing the Panel Template](#customizing-the-panel-template)  
- [Customizing the Product Template](#customizing-the-product-template)  
- [Troubleshooting](#troubleshooting)  
- [Credits and License](#credits-and-license)

---

## Features

- **Snippets**: Create and store Amazon products via a Wagtail snippet (ASIN, affiliate link, image, price, etc.).  
- **StreamField Integration**: Embed these snippets in any Wagtail page model using a custom `AmazonProductSnippetBlock`.  
- **One-Click Update**: A custom admin panel button to refresh product data directly from the Amazon API.  
- **Permissions**: Secure by default. Only users who can edit snippets can retrieve fresh product data.  

---

## Requirements

1. Python **3.8+**  
2. Django **5.2+**  
3. Wagtail **7.0+**  
4. An **Amazon Associates** account with access to PA-API

---

## Installation

1. **Install** the package (already in your project):
    ```bash
    pip install wagtail-amazon-paapi
    ```
2. **Add `wagtail_amazon_paapi`** to your `INSTALLED_APPS` in `settings.py`:
    ```python
    INSTALLED_APPS = [
        # ...
        'wagtail_amazon_paapi',
        # ...
    ]
    ```
3. **Migrate**:
    ```bash
    python manage.py makemigrations wagtail_amazon_paapi
    python manage.py migrate
    ```

---

## Configuration

In your Django project's `settings.py`, define the credentials for your Amazon Associates account under `WAGTAIL_AMAZON_PRODUCTS`:

```python
WAGTAIL_AMAZON_PRODUCTS = {
    "AMAZON_PAAPI_ACCESS_KEY": "YOUR_ACCESS_KEY",
    "AMAZON_PAAPI_SECRET_KEY": "YOUR_SECRET_KEY",
    "AMAZON_PAAPI_PARTNER_TAG": "YOUR_PARTNER_TAG",
    "AMAZON_PAAPI_COUNTRY": "US",
    # any other keys as needed
}
```

> **Security Tip:** Use environment variables or a secure key manager whenever possible. Avoid committing secrets to version control.

---

## Usage

### Creating Product Snippets

1. **In the Wagtail admin**, go to **Snippets** → **Amazon Product Snippets**.  
2. **Click "Add Amazon Product Snippet"**.  
3. **Enter the ASIN** (and optionally, a placeholder product title).  
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

---

## Customizing the Panel Template

By default, `amazon_update_panel.html` contains a button labeled **"Update From Amazon API"**. This button fetches the ASIN data from Amazon whenever clicked. If you wish to customize the look, text, or layout, edit the template:

```html
<!-- amazon_update_panel.html -->
{% load wagtailadmin_tags i18n %}
<div class="help-block">
  <p>{% trans "Click the button below to fetch updated data from Amazon." %}</p>
</div>
<a href="{% url 'wagtail_amazon_paapi:update_amazon_product' snippet.id %}" class="button button-longrunning">
  {% trans "Update From Amazon API" %}
</a>
```

When you reload the snippet edit page, the "Update from Amazon" button will have your custom text and layout.

---

## Customizing the Product Template

How an Amazon product snippet is displayed on your site is controlled by `amazon_product_snippet.html`. You can override this template in your own `templates` directory if you want a different design. The default usage is:

```html
{% with product=self.product %}
    <div class="amazon-product-snippet">
        {% if product.image_url %}
            <img src="{{ product.image_url }}" alt="{{ product.product_title }}">
        {% endif %}
        <h3>{{ product.product_title }}</h3>
        <p>Price: {{ product.price }}</p>
        <a href="{{ product.affiliate_url }}" target="_blank" rel="noopener sponsored">Buy on Amazon</a>
    </div>
{% endwith %}
```

---

## Troubleshooting

1. **Snippet Fails to Update:**  
   Check logs for API errors. Ensure your ASIN is correct and your Amazon credentials haven’t expired.  

2. **Rate Limits / Throttling:**  
   The `AmazonApi` call in `amazon_api.py` sets a default `throttling` parameter. Make sure you’re not calling the update button too frequently.  

3. **Snippets Admin URL Not Found:**  
   Confirm you’ve included `wagtail_amazon_paapi.urls` in your main urls.py. Also check `wagtail_hooks.py` to ensure the admin URLs are registered.  

4. **Empty Panel Template:**  
   If you don’t see the update button in your snippet edit page, you likely need to add content to amazon_update_panel.html as mentioned above.  

5. **Country Code / Config Issues:**  
   The code checks settings under `WAGTAIL_AMAZON_PRODUCTS`. Ensure your `country` code matches what the `amazon_paapi` library supports (e.g., `US`, `UK`, `DE`, etc.).  

---

## Credits and License

- **Author**: [Ravi Gupta](mailto:ravi.opensource@protonmail.com)  
- **License**: [MIT](https://opensource.org/licenses/MIT)  

This project is not affiliated with or endorsed by Amazon. Use of the AWS Product Advertising API is subject to Amazon Associates Program Policies. 

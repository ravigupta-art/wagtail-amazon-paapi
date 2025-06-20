from amazon_paapi import AmazonApi
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_product_data_from_api(asin: str):
    """
    Fetches product data from the Amazon API for a given ASIN.
    Returns a dictionary of the data or None if it fails.
    """
    try:
        # Get settings for our app, with a fallback to an empty dict
        app_settings = getattr(settings, 'WAGTAIL_AMAZON_PRODUCTS', {})

        # Get credentials from settings, or None if they don't exist
        access_key = app_settings.get('AMAZON_PAAPI_ACCESS_KEY')
        secret_key = app_settings.get('AMAZON_PAAPI_SECRET_KEY')
        partner_tag = app_settings.get('AMAZON_PAAPI_PARTNER_TAG')
        country = app_settings.get('AMAZON_PAAPI_COUNTRY')

        if not all([access_key, secret_key, partner_tag, country]):
            logger.error("WAGTAIL_AMAZON_PRODUCTS settings are not configured.")
            return None

        amazon = AmazonApi(
            key=access_key,
            secret=secret_key,
            tag=partner_tag,
            country=country,
            throttling=10, # Adjust throttling as needed
        )
        
        products = amazon.get_items(item_ids=[asin])
        
        if not products or not products.items:
            return None
            
        product = products.items[0]
        
        return {
            "product_title": product.item_info.title.display_value,
            "affiliate_url": product.detail_page_url,
            "image_url": product.images.primary.large.url if product.images else "",
            "price": product.offers.listings[0].price.display_amount if product.offers else "",
        }
        
    except Exception as e:
        logger.error(f"Amazon API call failed: {e}")
        return None
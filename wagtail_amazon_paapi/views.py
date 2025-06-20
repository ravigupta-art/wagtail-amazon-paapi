from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from wagtail.admin.auth import user_passes_test # Import the permission checker
from wagtail.snippets.models import get_snippet_models
from .models import AmazonProductSnippet
from .amazon_api import get_product_data_from_api

# Create your views here.

def get_snippet_edit_url(snippet_id):
    # Helper to find the correct snippet edit URL
    for model in get_snippet_models():
        if model == AmazonProductSnippet:
            return reverse(f'wagtailsnippets_{model._meta.app_label}_{model._meta.model_name}:edit', args=[snippet_id])
    return '/admin/' # Fallback

def can_edit_snippets(user):
    """Simple permission check - only staff or superusers can update products"""
    return user.is_active and (user.is_staff or user.is_superuser)

@user_passes_test(can_edit_snippets) # Replace @login_required
def update_amazon_product(request, snippet_id):
    snippet = get_object_or_404(AmazonProductSnippet, id=snippet_id)
    
    # Fetch new data from the API
    new_data = get_product_data_from_api(snippet.asin)
    
    if new_data:
        # Update the snippet fields with the new data
        snippet.product_title = new_data.get('product_title', snippet.product_title)
        snippet.affiliate_url = new_data.get('affiliate_url', snippet.affiliate_url)
        snippet.image_url = new_data.get('image_url', snippet.image_url)
        snippet.price = new_data.get('price', snippet.price)
        snippet.save()
        messages.success(request, f"Successfully updated product: {snippet.product_title}")
    else:
        messages.error(request, f"Failed to update product with ASIN: {snippet.asin}. The ASIN might be invalid or the API limit was reached.")
        
    # Redirect back to the snippet edit page
    return redirect(get_snippet_edit_url(snippet_id))
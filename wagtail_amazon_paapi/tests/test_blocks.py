import pytest
from wagtail_amazon_paapi.blocks import AmazonProductSnippetBlock


def test_amazon_product_snippet_block_uses_custom_form_template():
    block = AmazonProductSnippetBlock()
    assert (
        block.meta.form_template
        == "wagtail_amazon_paapi/blocks/amazon_product_snippet_form.html"
    )


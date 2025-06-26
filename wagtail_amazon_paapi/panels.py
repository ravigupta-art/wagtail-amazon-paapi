from wagtail.admin.panels import Panel

class AmazonUpdatePanel(Panel):
    class BoundPanel(Panel.BoundPanel):
        template_name = "wagtail_amazon_paapi/admin/panels/amazon_update_panel.html"

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            # This safely passes the snippet object to our template
            context["snippet"] = self.instance
            return context

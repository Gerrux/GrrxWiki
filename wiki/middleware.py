from wiki.singleton import SectionTree
from django.template.response import TemplateResponse


class NavbarFooterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        section_tree = SectionTree().tree

        response = self.get_response(request)

        if isinstance(response, TemplateResponse):
            response.context_data['section_tree'] = section_tree

        return response

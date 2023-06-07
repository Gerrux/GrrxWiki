from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from wiki.models import Article, Section


def index(request):
    return render(request, 'wiki/index.html')


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'wiki/article_detail.html', {'article': article})


class SectionDetailView(DetailView):
    model = Section
    template_name = 'wiki/section_detail.html'


def error_404_view(request, exception):
    return render(request, 'errors/404.html')

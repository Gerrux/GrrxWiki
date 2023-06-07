from django.urls import path

from wiki import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('sections/', views.get_sections_tree, name='sections_tree'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('sections/<int:pk>/', views.SectionDetailView.as_view(), name='section_detail'),
]

from django.contrib import admin

from wiki.models import Article, Section

admin.site.register(Section)
admin.site.register(Article)


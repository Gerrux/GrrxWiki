from django.db import models
from django.urls import reverse


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def get_ancestors(self):
        ancestors = []
        node = self.parent
        while node:
            ancestors.append(node)
            node = node.parent
        return ancestors

    def get_absolute_url(self):
        return reverse('section_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles')

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

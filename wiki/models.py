from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


class Photo(models.Model):
    image = models.ImageField(upload_to="photos/")


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def get_ancestors(self):
        ancestors = []
        node = self.parent
        while node:
            ancestors.append(node)
            node = node.parent
        return ancestors

    def get_absolute_url(self):
        return reverse("section_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="articles"
    )
    main_photo = models.ImageField(upload_to="article_photos/", blank=True)
    gallery_photos = models.ManyToManyField(Photo, related_name="articles", blank=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="articles_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="updated_articles",
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="article_comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_comments"
    )


class Moderation(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="moderations"
    )
    moderated_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="moderations"
    )
    moderated_at = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="histories"
    )
    changed_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="histories"
    )
    changed_at = models.DateTimeField(auto_now_add=True)
    content_before = models.TextField()
    content_after = models.TextField()


class Role(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="roles")


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    comments = models.ManyToManyField(ArticleComment, related_name="profiles")
    edits = models.IntegerField(default=0)

from django import forms
from .models import (
    Section,
    Article,
    ArticleComment,
    Moderation,
    History,
    Role,
    UserProfile,
)


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["title", "description", "parent"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "section", "main_photo", "gallery_photos"]

    widgets = {
        "main_photo": forms.ClearableFileInput(
            attrs={"multiple": True, "required": False}
        ),
    }


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]


class ModerationForm(forms.ModelForm):
    class Meta:
        model = Moderation
        fields = []


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = []


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["name"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["edits"]

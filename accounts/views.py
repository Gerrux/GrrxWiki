from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, UpdateProfileForm, CustomUserUpdateForm, CommentForm
from .models import CustomUser, Comment


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UpdateUserView(UpdateView):
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/update_user.html'

    def get_object(self):
        return self.request.user


class UpdateProfileView(UpdateView):
    form_class = UpdateProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/update_profile.html'

    def get_object(self):
        return self.request.user


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.profile = user
        comment.save()
        messages.success(request, 'Comment added successfully.')
        return redirect('profile', username=username)
    comments = Comment.objects.filter(profile=user)
    paginator = Paginator(comments, 10) # показывать 10 комментариев на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'registration/profile.html', {'form': form, 'user': user, 'page_obj': page_obj})

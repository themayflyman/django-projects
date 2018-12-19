from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Board, Post, Comment


class IndexView(generic.ListView):
    template_name = 'bbs/index.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        return Board.objects.all().order_by('x')


class BoardView(generic.ListView):
    template_name = 'bbs/board.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(board=self.kwargs['x'])


class NewPostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login'
    model = Post
    fields = ['subject', 'content', 'image']
    template_name = 'bbs/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.board_id = self.kwargs['x']
        self.success_url = reverse('bbs:board', args=(self.kwargs['x'],))

        return super(NewPostView, self).form_valid(form)


class PostView(generic.DetailView):
    model = Post
    template_name = 'bbs/post.html'


class CommentView(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login'
    model = Comment
    fields = ['content', 'image']
    template_name = 'bbs/comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        self.success_url = reverse('bbs:board', args=(self.kwargs['x'],))

        return super(CommentView, self).form_valid(form)

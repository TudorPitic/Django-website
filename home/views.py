from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# all of our data (posts and all) are in the database

def home(request):
    context = {
        'posts': Post.objects.all()
        # call posts from database
    }
    return render(request, 'home/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # anyone can see your post
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # inheritance explanation: you need to be logged in to create, create view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    # inheritance explanation: the post must be yours to update, you need to be logged in to update, update view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this function makes sure the author is the one updating the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    # inheritance explanation: the post must be yours to delete, you need to be logged in to delete, delete view
    # anyone can see your post
    model = Post
    success_url = '/'
    # this function makes sure the author is the one deleting the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'home/about.html', {'title': 'AboutTitle'})

def maps(request):
    return render(request, 'home/maps.html', {'title': 'MapsTitle'})

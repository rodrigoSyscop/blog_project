from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

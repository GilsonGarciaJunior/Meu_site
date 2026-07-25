from django.views.generic import ListView, DetailView
from ..models import Post


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "post_list"


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
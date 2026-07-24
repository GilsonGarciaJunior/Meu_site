from django.http import HttpResponse
from django.views import View


class PostList(View):
    def get(self, request):
        return HttpResponse("Hello World")


class PostDetail(View):
    def get(self, request, pk):
        return HttpResponse("Hello World")
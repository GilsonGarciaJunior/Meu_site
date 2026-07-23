import pytest
from django.urls import reverse

from blog.models import Post


@pytest.mark.django_db
def test_post_list():
    Post.objects.create(
        titulo="Primeiro Post",
        conteudo="Conteúdo do post"
    )

    response = client.get(reverse("post_list"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail(client):
    post = Post.objects.create(
        titulo="Primeiro Post",
        conteudo="Conteúdo do post"
    )

    response = client.get(
        reverse("post_detail", args=[post.pk])
    )

    assert response.status_code == 200
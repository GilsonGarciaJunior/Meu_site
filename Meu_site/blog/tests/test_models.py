import pytest

from blog.factories import PostFactory

pytestmark = pytest.mark.django_db


def test_cria_post():
    post = PostFactory()

    assert post.id is not None


def test_post_tem_titulo():
    post = PostFactory()

    assert post.titulo != ""


def test_post_tem_conteudo():
    post = PostFactory()

    assert post.conteudo != ""
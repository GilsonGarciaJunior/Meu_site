import factory

from .models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = factory.Faker("sentence")
    conteudo = factory.Faker("paragraph")
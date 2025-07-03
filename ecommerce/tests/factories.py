import factory
import pytest

from faker import Faker
from pytest_factoryboy import register
from ecommerce.inventory import models

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    # this may not genrate a unique name if used
    name = fake.lexify(text="cat_name_??????")

    # to genrate a number in sequence
    slug = factory.Sequence(lambda n: "cat_slug_%d" % n)


# Makes it avaliable
register(CategoryFactory)

import pytest
from ecommerce.inventory import models


# Testing the data in DB
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_invertory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


# Testing insertion in DB
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("Fashion_01", "Fashion_01", 1),
        ("Trainers_01", "Trainers_01", 1),
        ("Baseball_01", "Baseball_01", 1),
    ],
)
def test_invertory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

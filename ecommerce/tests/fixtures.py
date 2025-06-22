import pytest

@pytest.fixture
def cerate_admin_user(django_user_model):
    """
    Returns admin user in for the test db
    """

    return django_user_model.objects.create_superuser("admin","abc@a.com","password")
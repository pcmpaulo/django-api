import pytest

from core.users.models import User


def test_should_create_user(base_client):
    # GIVEN
    user = User.objects.create(
        first_name='John',
        last_name='Doe'
    )

    # WHEN
    response = base_client.get('/users/')
    data = response.json()

    # THEN
    assert len(data) == 1
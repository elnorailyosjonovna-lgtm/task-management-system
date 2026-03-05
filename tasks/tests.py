from django.test import TestCase

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_home_requires_login(client):
    r = client.get("/")
    assert r.status_code in (301, 302)


def test_login_page_loads(client):
    r = client.get(reverse("login"))
    assert r.status_code == 200


def test_user_can_login(client):
    User.objects.create_user(username="u1", password="pass12345")
    r = client.post(reverse("login"), {"username": "u1", "password": "pass12345"})
    assert r.status_code in (301, 302)


def test_admin_redirects(client):
    r = client.get("/admin/")
    assert r.status_code in (301, 302)


def test_logout_endpoint_exists(client):
    r = client.get(reverse("logout"))
    # Some Django versions return 405 for GET logout; others redirect. Either is OK.
    assert r.status_code in (301, 302, 405)

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class LogInTests(TestCase):
    def setUp(self):
        self.superUserCred = { "username": "testerSuper", "password": "password1.1" }
        self.normalUserCred = { "username": "ab@gm...ac", "password": "tenant!23#" }
        User.objects.create_superuser(self.superUserCred["username"], "", self.superUserCred["password"])
        User.objects.create_user(self.normalUserCred["username"], "", self.normalUserCred["password"])

    def test_invalid_login(self):
        self.client.get(reverse("logout"))
        response = self.client.post(reverse("login"), {"username": "ab@gm...", "password": self.normalUserCred["password"]}, follow=True)
        self.assertFalse(response.context["user"].is_authenticated)

    def test_incorrect_password(self):
        self.client.get(reverse("logout"))
        response = self.client.post((reverse("login")), {"username": self.normalUserCred["username"], "password": "tenant!23"}, follow=True)
        self.assertFalse(response.context["user"].is_authenticated)

    def test_superuser_login(self):
        self.client.get(reverse("logout"))
        response = self.client.post(reverse("login"), self.superUserCred, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertEquals(response.status_code, 200)

    def test_normaluser_login(self):
        self.client.get(reverse("logout"))
        response = self.client.post(reverse("login"), self.normalUserCred, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertRedirects(response, "/admin/login/?next=/admin/")
        self.assertContains(response, "class=\"errornote\"", html=False)


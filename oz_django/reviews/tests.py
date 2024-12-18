from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse

from .models import Review
from users.models import User
from feeds.models import Feed


class ReviewAPITestCase(APITestCase):
    def setUp(self):
        # User Model
        self.user = User.objects.create_user(username = "testuser", password = "password")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.token}")

        # Feed Model
        self.feed = Feed.objects.create(user = self.user, title = "New Title")

        # Review Model
        self.review1 = Review.objects.create(content = "Content 1", likes_num = 0, user = self.user, feed = self.feed)
        self.review2 = Review.objects.create(content = "Content 2", likes_num = 0, user = self.user, feed = self.feed)

    def test_get_all_reviews(self):
        url = reverse("reviews")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 2)

    def test_get_review_detail(self):
        url = reverse("review_detail", kwargs = {"review_id" : self.review1.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], self.review1.content)
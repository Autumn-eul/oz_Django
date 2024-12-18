from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User
from .models import Address
from rest_framework.authtoken.models import Token


class AddressAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "testuser", password = "password")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.address = Address.objects.create(
            street = "123 Main St",
            city = "Seoul",
            state = "Seoul",
            postal_code = "12345",
            country = "Korea",
            user = self.user
        )

    def test_get_addresses_unauthorized(self):
        self.client.logout()
        url = reverse('address_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_addresses(self):
        url = reverse("address_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_address(self):
        url = reverse("create_address", kwargs = {"user_id" : self.user.id})
        data = {
            'street': "99",
            'city': "강남구",
            'state': "서울시",
            'postal_code': "12346",
            'country': "대한민국",
            'user': self.user.id
        }
        response = self.client.post(url, data)
        print("Response Status:", response.status_code)
        print("Response Data:", response.data) # 디버깅용 출력
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Address.objects.filter(street = "99").exists())


    def test_update_address(self):
        url = reverse("update_address", kwargs = {"address_id" : self.address.id})
        data = {
            'street': "99-8",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "99-8")

    def test_delete_address(self):
        url = reverse("delete_address", kwargs = {"address_id" : self.address.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Address.objects.filter(pk = self.address.pk).exists())
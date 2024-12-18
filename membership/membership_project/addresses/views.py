from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .models import Address
from .serializers import AddressSerializer

class AddressList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many = True)
        return Response(serializer.data)

class AddressDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, address_id):
        try:
            return Address.objects.get(id = address_id)
        except Address.DoesNotExist:
            raise NotFound

    def get(self, request, address_id):
        try:
            address = self.get_object(address_id)
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        except:
            return Response({'error': 'Address not found'}, status = status.HTTP_404_NOT_FOUND)

class CreateAddress(APIView):
    def post(self, request, user_id):
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            raise NotFound

        data = request.data.copy() # 데이터 복사 후 수정
        data["user"] = user.id # user 필드 추가
        serializer = AddressSerializer(data = data)

        if serializer.is_valid():
            serializer.save(user = user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UpdateAddress(APIView):
    def get_object(self, address_id):
        try:
            return Address.objects.get(id = address_id)
        except Address.DoesNotExist:
            raise NotFound

    def put(self, request, address_id):
        address = self.get_object(address_id)
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DeleteAddress(APIView):
    def get_object(self, address_id):
        try:
            return Address.objects.get(id = address_id)
        except Address.DoesNotExist:
            raise NotFound

    def delete(self, request, address_id):
        address = self.get_object(address_id)
        if address is None:
            return Response({'error': 'Address not found'}, status = status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


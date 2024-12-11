from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import ModelSerializer, MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# api/v1/users[POST] => 유저 생성 API
class Users(APIView):
    def post(self, request):
        # passowrd -> 검증을 해야하고, 해시화 해서 저장 필요
        # the other -> 비밀번호 외 다른 데이터들

        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data = request.data)

        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")

        if serializer.is_valid():
            user = serializer.save() # 새로운 유저를 생성
            user.set_password(password) # set_password : 비밀번호를 해시화 하는 함수
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)

        else:
            raise ParseError(serializer.errors)
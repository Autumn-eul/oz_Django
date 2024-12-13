from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("", views.AddressList.as_view(), name = "address_list"),
    path("<int:address_id>/", views.AddressDetail.as_view(), name = "address_detail"),
    path("create/<int:user_id>/", views.CreateAddress.as_view(), name = "create_address"),
    path("update/<int:address_id>/", views.UpdateAddress.as_view(), name = "update_address"),
    path("delete/<int:address_id>/", views.DeleteAddress.as_view(), name = "delete_address"),
    path("getToken", obtain_auth_token),

    # Simple JWT Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]
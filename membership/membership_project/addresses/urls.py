from django.urls import path
from . import views

urlpatterns = [
    path("", views.AddressList.as_view(), name = "address_list"),
    path("<int:address_id>/", views.AddressDetail.as_view(), name = "address_detail"),
    path("create/<int:user_id>/", views.CreateAddress.as_view(), name = "create_address"),
    path("update/<int:address_id>/", views.UpdateAddress.as_view(), name = "update_address"),
    path("delete/<int:address_id>/", views.DeleteAddress.as_view(), name = "delete_address"),
]
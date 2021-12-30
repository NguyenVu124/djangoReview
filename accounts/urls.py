from django.urls import path

from .views import UserCreateAPIView, UserDetailAPIView, UserListAPIView,AuthInfo

app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
    path('oauth2-info/', AuthInfo.as_view(),name="auth_info")
]

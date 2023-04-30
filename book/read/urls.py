from django.urls import include, path
from read.views import CustomUserViewSet, ReadView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', ReadView, basename='books')
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

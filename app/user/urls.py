from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from user import views

app_name = 'user'

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserViewSet)


urlpatterns = [
    path('hello/', views.HelloAPIView.as_view(), name='hello'),
    path('', include(router.urls))
]

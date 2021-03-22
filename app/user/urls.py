from django.urls import path

from user import views

app_name = 'user'


urlpatterns = [
    path('hello/', views.HelloAPIView.as_view(), name='hello'),
]

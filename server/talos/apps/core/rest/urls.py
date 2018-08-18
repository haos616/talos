from django.urls import path

from .views import AuthApiView


urlpatterns = [
    path('', AuthApiView.as_view()),
]

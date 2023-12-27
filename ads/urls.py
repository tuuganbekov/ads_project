from django.urls import path

from .views import CategoryAPIView, AdAPIView

urlpatterns = [
    path("categories/", CategoryAPIView.as_view()),
    path("", AdAPIView.as_view()),
]
from django.urls import path

from .views import CategoryAPIView, AdAPIView, AdDetailAPIView

urlpatterns = [
    path("categories/", CategoryAPIView.as_view()),
    path("", AdAPIView.as_view()),
    path("detail/<int:pk>/", AdDetailAPIView.as_view()),
]
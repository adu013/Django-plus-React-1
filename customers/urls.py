from django.urls import path

from .apiviews import CustomerListCreateAPIView


urlpatterns = [
    path('api/customers/', CustomerListCreateAPIView.as_view()),
]

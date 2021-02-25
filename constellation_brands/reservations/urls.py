from django.urls import path

from .views import (
    Home,
    CreateReservation,
    DetailReservation,
    UpdateReservation,
    DeleteReservation,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create/", CreateReservation.as_view(), name="create"),
    path("read/", DetailReservation.as_view(), name="detail"),
    path("update/<int:pk>/", UpdateReservation.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteReservation.as_view(), name="delete"),
]
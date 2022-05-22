from django.urls import path
from . import views

urlpatterns = [
    path("", views.VestidoListView.as_view(), name="vestidos"),
]

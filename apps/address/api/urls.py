from django.urls import path
from .views import RegionApiView

urlpatterns = [
    path("get-regions/", RegionApiView.as_view(), name="get-regions")
]

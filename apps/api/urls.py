from django.urls import path, include

urlpatterns = [
    path("address/", include("address.api.urls"))
]

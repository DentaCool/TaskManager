from django.urls import include, path

from backend.api.urls import router

urlpatterns = [path("api/", include("backend.api.urls"), name="api")]

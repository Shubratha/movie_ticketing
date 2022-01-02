from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cinemas/", include("inventory.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("user.urls")),
    path("book/", include("booking.urls")),
]

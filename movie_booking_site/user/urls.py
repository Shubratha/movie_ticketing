from django.urls import include, path

from . import views

urlpatterns = [path("register/", views.RegisterUser.as_view())]

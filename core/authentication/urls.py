from django.urls import path
from authentication.views import AuthenticationService

urlpatterns = [
    path("login", AuthenticationService.as_view({"get": "list"}), name="login")
]

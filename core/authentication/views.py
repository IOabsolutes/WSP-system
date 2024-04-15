from django.shortcuts import render
from rest_framework.response import Response
from rest_framework

# Create your views here.
class AuthenticationService():

    def list(self, request, *args, **kwargs):
        return Response({"message": "Hello, world!"}, status=200)

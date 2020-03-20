from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

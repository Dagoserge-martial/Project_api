from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from .models import *
from .serializers import User_coursSerializer, CoursSerializer, ChapitreSerializer, ModuleSerializer, MoisSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class MoisViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Mois.objects.all()
    serializer_class = MoisSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer

class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class User_coursViewSet(viewsets.ModelViewSet):
    queryset = User_cours.objects.all()
    serializer_class = User_coursSerializer
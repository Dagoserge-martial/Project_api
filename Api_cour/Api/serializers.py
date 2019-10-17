
from rest_framework import serializers

from .models import *
from drf_dynamic_fields import DynamicFieldsMixin

class User_coursSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_cours
        fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'

class ChapitreSerializer(serializers.ModelSerializer):
    chapitre_cours = CoursSerializer(many=True, required=False)
    class Meta:
        model = Chapitre
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    module_chapitre = ChapitreSerializer(many=True, required=False)
    module_user = User_coursSerializer(many=True, required=False)
    class Meta:
        model = Module
        fields = '__all__'

class MoisSerializer(serializers.ModelSerializer):
    mois_module = ModuleSerializer(many=True, required=False)
    class Meta:
        model = Mois
        fields = '__all__'

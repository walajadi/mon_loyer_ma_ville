"""
    Villes models
"""
# pylint:disable=too-few-public-methods

from django.db import models
from rest_framework import serializers

from core.models import BaseModel
from helpers.geoloc import ApiGeoloc


class Ville(BaseModel):
    """
    Base class model
    """

    code_insee = models.CharField(
        null=True, max_length=128, help_text="Code INSEE de la ville."
    )
    nom = models.CharField(null=True, max_length=256, help_text="Nom de la ville.")
    departement = models.CharField(
        null=True, max_length=128, help_text="Departement de la ville."
    )
    loyer_moyen = models.FloatField(null=True, help_text="Loyer moyen.")


class VilleSerializer(serializers.ModelSerializer):
    """
    Ville serializer
    """

    code_postal = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class.
        """

        model = Ville
        exclude = ("created_at", "updated_at", "id", "deleted")

    def get_code_postal(self, instance):
        """
        Serializer method
        """
        return ApiGeoloc().get_code_pos(instance)


class RequestSerializer(serializers.Serializer):  # pylint:disable= abstract-method
    """
    Request Serilalizer.
    """

    surface = serializers.ListSerializer(child=serializers.FloatField(), required=True)
    loyer_max = serializers.ListSerializer(
        child=serializers.FloatField(), required=True
    )

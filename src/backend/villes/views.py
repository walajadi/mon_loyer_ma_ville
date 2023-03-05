"""
Villes views.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http.response import JsonResponse

from villes.models import Ville, VilleSerializer, RequestSerializer
from core.permissions import PermissionAccess


class VillesViewSet(viewsets.ModelViewSet):  # pylint:disable=too-many-ancestors
    """
    Villes viewset
    """

    queryset = Ville.objects.filter(deleted=False)  # pylint:disable= no-member
    serializer_class = VilleSerializer
    permission_classes = [PermissionAccess]

    # GET villes/<code_departement>/
    def retrieve(self, request, pk=None, **kwargs):  # pylint: disable=arguments-differ
        """
        process request to retrieve cities, given the loyer_moyen.
        """
        params = request.query_params
        request_data = RequestSerializer(data=dict(params))
        request_data.is_valid(raise_exception=True)

        surface = float(params.get("surface"))
        loyer_max = float(params.get("loyer_max"))

        if not all((loyer_max, surface)):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Invalid parameters"},
            )
        loyer_moyen_espere = loyer_max / surface
        query_set = self.queryset.filter(
            departement=pk, loyer_moyen__lt=loyer_moyen_espere
        )
        if not query_set.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = VilleSerializer(query_set, many=True).data
        return JsonResponse(data=data, safe=False)

"""
 Command file
"""

import os

from django.core.management.base import BaseCommand

from villes.models import Ville


class Command(BaseCommand):
    """
    Command Management
    """

    help = "Init villes databases"

    def handle(self, *args, **options):
        """
        - read data file and init cities database.

        Ex:
        id_zone;INSEE;LIBGEO;DEP;REG;EPCI;TYPPRED;loypredm2;
        lwr.IPm2;upr.IPm2;R2adj;NBobs_maille;NBobs_commune
        2362;1001;L'Abergement-Cl�menciat;1;84;200069193;maille;9,372335348;
        7,409663525;11,85487972;0,774249278;701;2
        """
        path = os.path.abspath("data/indicateurs-loyers-appartements.csv")
        with open(path, "r", encoding="latin-1") as _input_file:
            lines = _input_file.readlines()[1:]
            for _l in lines:
                _l = _l.split(";")
                Ville(
                    **{
                        "code_insee": _l[1],
                        "nom": _l[2],
                        "departement": _l[3],
                        "loyer_moyen": float(_l[7].replace(",", ".")),
                    }
                ).save()

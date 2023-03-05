"""
Get geoloc info from api.
"""

import requests

API_GEOLIC_URL = "https://geo.api.gouv.fr/communes"
TIMEOUT = 10


class ApiGeoloc:  # pylint: disable= too-few-public-methods
    """
    Geoloc class
    """

    def get_code_pos(self, ville):
        """
        Get code postal.
        """
        url = "{}/{}/".format(API_GEOLIC_URL, ville.code_insee)
        res = requests.get(url, timeout=TIMEOUT)
        if res.status_code != 200:
            return "NON TROUVE"
        return res.json()["codesPostaux"][0]

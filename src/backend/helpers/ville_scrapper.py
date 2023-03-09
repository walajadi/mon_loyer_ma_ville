"""
    Ville Scrapper.
"""
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


class VilleScrapper:
    """
    Ville Scrapper.
    """

    CITY_INFO_URL = "https://www.bien-dans-ma-ville.fr"
    UNKNOW_VALUE = "INCONNU"
    session = requests.Session()

    def __init__(self, ville):
        """
        init class
        """
        self._ville_name = ville.nom.lower()
        self._insee_code = ville.code_insee

        self._nbr_habitant = None
        self._note_ville = None

    def __call__(self, *args, **kwargs):
        """
        Get info on call.
        """
        ville_url = "{}/{}-{}/".format(
            self.CITY_INFO_URL, self._ville_name.lower(), self._insee_code
        )
        res = self.session.get(ville_url)
        if res.status_code != 200:
            self._nbr_habitant = self.UNKNOW_VALUE
            self._note_ville = self.UNKNOW_VALUE
            return self
        html_content = res.content
        # get nbr habitants
        habitant_soup = BeautifulSoup(html_content, features="html.parser")
        bloc_chiffre = habitant_soup.find("table", class_="bloc_chiffre")
        if bloc_chiffre is None:
            self._nbr_habitant = self.UNKNOW_VALUE
        nombre_hab = bloc_chiffre.find("tr").find_all("td")[1].text
        self._nbr_habitant = nombre_hab

        # get note
        note_url = "{}/avis.html".format(ville_url)
        note_res = self.session.get(note_url)
        note_soup = BeautifulSoup(note_res.content, features="html.parser")
        bloc_note = note_soup.find("div", class_="total")
        if bloc_note is None:
            self._note_ville = self.UNKNOW_VALUE
            return self
        self._note_ville = bloc_note.text
        return self

    @property
    def note_vile(self):
        """
        Note ville
        """
        return self._note_ville

    @property
    def habitants(self):
        """
        habitants
        """
        return self._nbr_habitant


def scrap_one(_ville):
    """
    Scrap given a city.
    """
    scrapper = VilleScrapper(_ville)()
    return {
        "code_insee": _ville.code_insee,
        "habitants": scrapper.habitants,
        "note": scrapper.note_vile,
    }


def scrap_all(villes):
    """
    Create a thread pool and get note + habitants
    """

    with ThreadPoolExecutor(max_workers=60) as executor:
        return executor.map(scrap_one, villes, timeout=20)

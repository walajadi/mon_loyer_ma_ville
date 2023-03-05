"""
    Ville Scrapper.
"""
from bs4 import BeautifulSoup


class VilleScrapper:
    """
    Ville Scrapper.
    """

    CITY_INFO_URL = "https://www.bien-dans-ma-ville.fr"
    UNKNOW_VALUE = "INCONNU"

    def __init__(self, ville, session):
        """
        init class
        """
        self._ville_name = ville.nom.lower()
        self._insee_code = ville.code_insee

        self._nbr_habitant = None
        self._note_ville = None
        self._session = session

    def __call__(self, *args, **kwargs):
        """
        Get info on call.
        """
        ville_url = "{}/{}-{}/".format(
            self.CITY_INFO_URL, self._ville_name.lower(), self._insee_code
        )
        res = self._session.get(ville_url)
        if res.status_code != 200:
            self._nbr_habitant = self.UNKNOW_VALUE
            self._note_ville = self.UNKNOW_VALUE
            return self
        html_content = res.content
        habitant_soup = BeautifulSoup(html_content, features="html.parser")
        bloc_chiffre = habitant_soup.find("table", class_="bloc_chiffre")
        if bloc_chiffre is None:
            self._nbr_habitant = self.UNKNOW_VALUE
        nombre_hab = bloc_chiffre.find("tr").find_all("td")[1].text
        self._nbr_habitant = nombre_hab

        # chercher la note
        note_url = "{}/avis.html".format(ville_url)
        note_res = self._session.get(note_url)
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

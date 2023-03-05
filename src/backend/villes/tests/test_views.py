"""
 Test view
"""

from unittest.mock import patch
from requests import Session
import mock

from django.test import TestCase
from villes.models import Ville


class VilleTestCase(TestCase):
    """
    Ville test class
    """

    def setUp(self):
        """
        Setup test
        """
        self.my_city = Ville.objects.create(
            nom="Stains",
            code_insee="93240",
            departement=93,
            loyer_moyen=16.0,
        )

    def test_attribute(self):
        """
        Test Attribute
        """
        assert self.my_city.nom == "Stains"
        assert self.my_city.code_insee == "93240"
        assert len(Ville.objects.all()) == 1

    @patch.object(Session, "get")
    def test_call_ok(self, mock_sess_get):
        """
        Test OK + mock scrapper.
        """
        mock_sess_get.return_value = mock.MagicMock(
            status_code=200,
            content="""
            <table class="bloc_chiffre">
                <tbody>
                    <tr>
                        <td>Nombre d'habitants</td>
                        <td>21 528</td>
                        <td><a class="insee_voir_classement" href="https://www.bien-dans-ma-ville.fr/ ... ">Classement</a></td>
                </tbody>
            </table>
            <div class="bloc_notemoyenne">
                <h3>Note moyenne</h3>
                <div class="total">3.4<span>/5</span></div>
            </div>
            """,
        )

        request = self.client.get(
            "http://testserver/api/villes/93/?surface=40&loyer_max=800"
        )
        assert request.status_code == 200
        res = request.json()
        assert len(res) == 1
        assert res[0]["note"] == "3.4/5"
        assert res[0]["nom"] == "Stains"
        assert res[0]["departement"] == "93"
        assert res[0]["loyer_moyen"] == 16.0
        assert res[0]["habitants"] == "21 528"

        assert mock_sess_get.called

    def test_call_400(self):
        """
        max_loyer au lieu de loyer_max => BAD PARAM
        """
        request = self.client.get(
            "http://testserver/api/villes/93/?surface=40&max_loyer=800"
        )
        assert request.status_code == 400

    def test_call_404(self):
        """
        Pas de ville trouvee pour un loyer bas.
        """
        request = self.client.get(
            "http://testserver/api/villes/93/?surface=40&loyer_max=200"
        )
        assert request.status_code == 404

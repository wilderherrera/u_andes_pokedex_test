from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from pokedex.models import Pokemon


class PokemonViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.pokemon = Pokemon.objects.create(id=1, name="Bulbasaur")

    @patch('pokedex.views.v1.pokemon_views.PokemonService.get_by_id_or_name')
    def test_get_pokemon_by_id(self, mock_get_by_id_or_name):
        mock_get_by_id_or_name.return_value = self.pokemon

        response = self.client.get('/api/v1/pokemons/1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['name'], "Bulbasaur")
        mock_get_by_id_or_name.assert_called_once_with('1')

    @patch('pokedex.views.v1.pokemon_views.PokeApiService.get_all_pokemon')
    def test_get_all_pokemons(self, mock_get_all_pokemon):
        mock_response = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
                {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
            ]
        }
        mock_get_all_pokemon.return_value = mock_response

        response = self.client.get('/api/v1/pokemons')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['results'][0]['name'], "bulbasaur")
        mock_get_all_pokemon.assert_called_once_with(limit=20, offset=0)

    @patch('pokedex.views.v1.pokemon_views.PokemonService.update_pokemon')
    def test_patch_pokemon(self, mock_update_pokemon):
        updated_pokemon = Pokemon(id=1, name="Bulbasaur Updated")
        mock_update_pokemon.return_value = updated_pokemon

        update_data = {
            "name": "Bulbasaur Updated"
        }

        response = self.client.patch('/api/v1/pokemons/1', data=update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['name'], "Bulbasaur Updated")
        mock_update_pokemon.assert_called_once_with('1', update_data)

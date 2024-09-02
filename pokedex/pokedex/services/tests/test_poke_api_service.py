import unittest
from unittest.mock import patch

from pokedex.services.poke_api_service import PokeApiService


class PokeApiServiceTest(unittest.TestCase):

    @patch('pokedex.services.poke_api_service.requests.get')
    def test_get_all_pokemon(self, mock_get):
        mock_response_data = {
            "count": 1118,
            "next": "https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20",
            "previous": None,
            "results": [
                {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
                {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
            ]
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        service = PokeApiService()
        result = service.get_all_pokemon(limit=2, offset=0)

        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/', params={'limit': 2, 'offset': 0})

        self.assertEqual(len(result['results']), 2)
        self.assertEqual(result['results'][0]['name'], 'bulbasaur')
        self.assertEqual(result['results'][1]['name'], 'ivysaur')

    @patch('pokedex.services.poke_api_service.requests.get')
    def test_get_pokemon_by_id(self, mock_get):
        mock_response_data = {
            "id": 1,
            "name": "bulbasaur",
            "base_experience": 64,
            "height": 7,
            "is_default": True,
            "order": 1,
            "weight": 69,
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        service = PokeApiService()
        result = service.get_pokemon_by_id(1)

        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/1')

        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'bulbasaur')

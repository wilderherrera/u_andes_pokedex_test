from unittest.mock import patch, MagicMock

from django.http import HttpResponse
from django.test import TestCase, RequestFactory

from pokedex.middleware.get_pokedex_information_middleware import GetPokedexInformationMiddleware


class GetPokedexInformationMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.get_response_mock = MagicMock(return_value=HttpResponse("OK"))
        self.middleware = GetPokedexInformationMiddleware(self.get_response_mock)

    @patch('pokedex.repositories.pokemon_repository.PokemonRepository')
    @patch('pokedex.services.poke_api_service.PokeApiService')
    def test_middleware_creates_pokemon_if_not_exists(self, MockPokeApiService, MockPokemonRepository):
        mock_pokemon_repository = MockPokemonRepository.return_value
        mock_poke_api_service = MockPokeApiService.return_value

        mock_pokemon_repository.exists_by_id.return_value = False
        mock_pokemon_repository.exists_by_name.return_value = False

        mock_pokemon_info = {
            "id": 1,
            "name": "bulbasaur",
            "moves": [{"name": "tackle"}],
            "types": [{"name": "grass"}],
            "sprites": {
                "back_default": "url",
                "front_default": "url"
            }
        }
        mock_poke_api_service.get_pokemon_by_id.return_value = mock_pokemon_info

        request = self.factory.get('/api/v1/pokemons/1/')

        response = self.middleware.__call__(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")

    @patch('pokedex.repositories.pokemon_repository.PokemonRepository')
    @patch('pokedex.services.poke_api_service.PokeApiService')
    def test_middleware_does_not_create_pokemon_if_exists(self, MockPokeApiService, MockPokemonRepository):
        mock_pokemon_repository = MockPokemonRepository.return_value

        mock_pokemon_repository.exists_by_id.return_value = True

        request = self.factory.get('/api/v1/pokemons/2/')

        response = self.middleware.__call__(request)

        MockPokeApiService.return_value.get_pokemon_by_id.assert_not_called()
        mock_pokemon_repository.create_pokemon_with_details.assert_not_called()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")

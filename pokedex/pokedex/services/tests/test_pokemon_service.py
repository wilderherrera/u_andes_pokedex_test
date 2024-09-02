import unittest
from unittest.mock import patch, MagicMock

from pokedex.models import Pokemon
from pokedex.services.pokemon_service import PokemonService


class TestPokemonService(unittest.TestCase):
    def setUp(self):
        self.pokemon_service = PokemonService()

    @patch('pokedex.repositories.pokemon_repository.PokemonRepository.get_by_id_or_name')
    def test_get_by_id_or_name_exists(self, get_by_id_or_name):
        mock_pokemon = MagicMock(spec=Pokemon)
        mock_pokemon.id = 1
        mock_pokemon.name = "Bulbasaur"
        self.pokemon_service.get_by_id_or_name(1)
        get_by_id_or_name.assert_called_with(mock_pokemon.id)

    @patch('pokedex.repositories.pokemon_repository.PokemonRepository.update')
    def test_update(self, update):
        data = {}
        mock_pokemon = MagicMock(spec=Pokemon)
        mock_pokemon.id = 1
        mock_pokemon.name = "Bulbasaur"
        self.pokemon_service.update_pokemon(1, data)
        update.assert_called_with(mock_pokemon.id, data)

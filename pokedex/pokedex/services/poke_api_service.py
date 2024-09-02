import requests

from pokedex.serializers.pokedex_pokemon_serializer import PokedexPokemonSerializer
from pokedex.serializers.pokemon_list_serializer import PokemonDataSerializer


class PokeApiService:
    def __init__(self):
        self.base_path = "https://pokeapi.co/api/v2/pokemon/"

    def get_all_pokemon(self, limit=20, offset=0) -> [PokemonDataSerializer]:
        response = requests.get(self.base_path, params={"limit": limit, "offset": offset})
        return PokemonDataSerializer(response.json()).data

    def get_pokemon_by_id(self, pokemon_id: int) -> PokedexPokemonSerializer:
        response = requests.get(self.base_path + str(pokemon_id))
        return PokedexPokemonSerializer(response.json()).data

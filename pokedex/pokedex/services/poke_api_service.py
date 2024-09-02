import requests

from pokedex.serializers.pokemon_list_serializer import PokemonDataSerializer
from pokedex.serializers.pokemon_serializer import PokemonSerializer


class PokeApiService:
    def __init__(self):
        self.base_path = "https://pokeapi.co/api/v2/pokemon/"

    def get_all_pokemon(self, limit=20, offset=0) -> [PokemonDataSerializer]:
        response = requests.get(self.base_path, params={"limit": limit, "offset": offset})
    
        return PokemonDataSerializer(response.json()).data

    def get_pokemon_by_id(self, pokemon_id: int) -> PokemonSerializer:
        response = requests.get(self.base_path + str(pokemon_id))
        return PokemonSerializer(response.json()).data

    def get_pokemon_by_name(self, pokemon_name: str) -> PokemonSerializer:
        response = requests.get(self.base_path + pokemon_name)
        return PokemonSerializer(response.json()).data

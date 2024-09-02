import requests

from pokedex.serializers.pokedex_pokemon_serializer import PokedexPokemonSerializer
from pokedex.serializers.pokemon_list_serializer import PokemonDataSerializer


class PokeApiService:
    """
    A service class that interacts with the PokeAPI to retrieve Pokémon data.
    """

    def __init__(self):
        """
        Initializes the PokeApiService with the base URL for the PokeAPI.
        """
        self.base_path = "https://pokeapi.co/api/v2/pokemon/"

    def get_all_pokemon(self, limit=20, offset=0) -> [PokemonDataSerializer]:
        """
        Retrieves a list of Pokémon from the PokeAPI.

        Args:
            limit (int): The maximum number of Pokémon to retrieve. Defaults to 20.
            offset (int): The number of Pokémon to skip before starting to collect the result set. Defaults to 0.

        Returns:
            list: A list of Pokémon data serialized by PokemonDataSerializer.
        """
        response = requests.get(self.base_path, params={"limit": limit, "offset": offset})
        return PokemonDataSerializer(response.json()).data

    def get_pokemon_by_id(self, pokemon_id: int) -> PokedexPokemonSerializer:
        """
        Retrieves detailed information about a specific Pokémon by its ID.

        Args:
            pokemon_id (int): The ID of the Pokémon to retrieve.

        Returns:
            dict: The details of the Pokémon serialized by PokedexPokemonSerializer.
        """
        response = requests.get(self.base_path + str(pokemon_id))
        return PokedexPokemonSerializer(response.json()).data

from pokedex.repositories.pokemon_repository import PokemonRepository
from pokedex.services.poke_api_service import PokeApiService


class GetPokedexInformationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        response = self.get_response(request)
        if path.startswith('/api/v1/pokemons/'):
            pokemon_id = path.split('/')[4]
            pokemon_repository = PokemonRepository()
            if not (pokemon_repository.exists_by_id(pokemon_id)):
                poke_api_service = PokeApiService()
                pokemon_info = poke_api_service.get_pokemon_by_id(pokemon_id)
                pokemon_repository.create_pokemon_with_details(pokemon_info)
        return response

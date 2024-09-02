from django.db import transaction

from pokedex.repositories.pokemon_repository import PokemonRepository
from pokedex.services.poke_api_service import PokeApiService


class GetPokedexInformationMiddleware:
    """
    Middleware to automatically fetch and store Pokémon information if it does not exist in the database.

    This middleware intercepts requests to the Pokémon API endpoint and checks whether the Pokémon
    identified by the ID or name in the URL exists in the database. If the Pokémon does not exist,
    it fetches the information from an external API and stores it in the database.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware with the next middleware or view in the Django request/response cycle.

        Args:
            get_response (callable): The next middleware or view in the Django request/response cycle.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes the incoming request to check and fetch Pokémon data if necessary.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The response returned by the next middleware or view.

        The middleware checks the URL path to determine if it is a Pokémon API request.
        If the request path starts with `/api/v1/pokemons/`, the middleware extracts the Pokémon ID or name
        from the URL, checks if the Pokémon exists in the database, and if not, fetches it from an external API.
        """
        path = request.path

        if path.startswith('/api/v1/pokemons/'):
            pokemon_id = path.split('/')[4]
            pokemon_repository = PokemonRepository()
            poke_api_service = PokeApiService()

            with transaction.atomic():
                if pokemon_id.isdigit():
                    pokemon_id = int(pokemon_id)
                    if not pokemon_repository.exists_by_id(pokemon_id):
                        pokemon_info = poke_api_service.get_pokemon_by_id(pokemon_id)
                        pokemon_repository.create_pokemon_with_details(pokemon_info)
                else:
                    if not pokemon_repository.exists_by_name(pokemon_id):
                        pokemon_info = poke_api_service.get_pokemon_by_id(pokemon_id)
                        pokemon_repository.create_pokemon_with_details(pokemon_info)

        response = self.get_response(request)
        return response

from rest_framework.views import APIView

from pokedex.common.json_response import JsonResponse
from pokedex.services.poke_api_service import PokeApiService


class PokemonViews(APIView):
    def __init__(self):
        self.pokedex_service = PokeApiService()

    def get(self, request, pokemon_id=None, pokemon_name=None):
        if pokemon_id != None:
            return JsonResponse(self.pokedex_service.get_pokemon_by_id(pokemon_id), safe=False)
        if pokemon_name != None:
            return JsonResponse(self.pokedex_service.get_pokemon_by_name(pokemon_name), safe=False)

        limit = request.GET.get('limit', 20)
        offset = request.GET.get('offset', 0)
        return JsonResponse(self.pokedex_service.get_all_pokemon(limit=limit, offset=offset), safe=False)

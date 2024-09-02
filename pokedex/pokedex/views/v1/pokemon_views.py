import json

from rest_framework import status
from rest_framework.views import APIView

from pokedex.common.json_response import JsonResponse
from pokedex.serializers.models.pokemon_serializer import PokemonSerializer
from pokedex.services.poke_api_service import PokeApiService
from pokedex.services.pokemon_service import PokemonService


class PokemonViews(APIView):
    def __init__(self):
        self.pokedex_service = PokeApiService()
        self.pokemon_service = PokemonService()

    def get(self, request, pokemon_id=None, pokemon_name=None):
        if pokemon_id != None:
            return JsonResponse(PokemonSerializer(self.pokemon_service.get_by_id_or_name(pokemon_id)).data)
        limit = request.GET.get('limit', 20)
        offset = request.GET.get('offset', 0)
        return JsonResponse(self.pokedex_service.get_all_pokemon(limit=limit, offset=offset), status=status.HTTP_200_OK)

    def patch(self, request, pokemon_id=None):
        data = json.loads(request.body)
        return JsonResponse(PokemonSerializer(self.pokemon_service.update_pokemon(pokemon_id, data)).data,
                            status=status.HTTP_200_OK)

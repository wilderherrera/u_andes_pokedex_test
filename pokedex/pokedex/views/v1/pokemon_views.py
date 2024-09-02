import json

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('limit', openapi.IN_QUERY, description="Limit the number of results",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('offset', openapi.IN_QUERY, description="Offset for pagination",
                              type=openapi.TYPE_INTEGER)
        ],
        responses={200: PokemonSerializer(many=True)}
    )
    def get(self, request, pokemon_id=None):
        if pokemon_id != None:
            return JsonResponse(PokemonSerializer(self.pokemon_service.get_by_id_or_name(pokemon_id)).data)
        limit = request.GET.get('limit', 20)
        offset = request.GET.get('offset', 0)
        return JsonResponse(self.pokedex_service.get_all_pokemon(limit=limit, offset=offset), status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=PokemonSerializer,
        responses={200: PokemonSerializer(), 400: 'Bad Request'}
    )
    def patch(self, request, pokemon_id=None):
        try:
            data = json.loads(request.body)
            updated_pokemon = self.pokemon_service.update_pokemon(pokemon_id, data)
            return JsonResponse(PokemonSerializer(updated_pokemon).data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred: " + str(e)},
                                status=status.HTTP_400_BAD_REQUEST)

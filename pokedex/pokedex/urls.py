from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from pokedex.views.v1.pokemon_views import PokemonViews

schema_view = get_schema_view(
    openapi.Info(
        title="Pokedex API",
        default_version='v1',
        description="API documentation for the Pokedex project",
        contact=openapi.Contact(email="contact@pokedex.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('api/v1/pokemons', PokemonViews.as_view(), name='pokemon-list'),
    path('api/v1/pokemons/<str:pokemon_id>', PokemonViews.as_view(), name='pokemon-details-id'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

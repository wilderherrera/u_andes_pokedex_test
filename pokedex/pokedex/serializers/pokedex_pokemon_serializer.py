from rest_framework import serializers


class MoveSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class PokemonMoveSerializer(serializers.Serializer):
    name = serializers.CharField(source='move.name', max_length=100)


class SpriteDetailSerializer(serializers.Serializer):
    front_default = serializers.URLField(allow_null=True, required=False)
    front_female = serializers.URLField(allow_null=True, required=False)
    front_shiny = serializers.URLField(allow_null=True, required=False)
    front_shiny_female = serializers.URLField(allow_null=True, required=False)
    back_default = serializers.URLField(allow_null=True, required=False)
    back_female = serializers.URLField(allow_null=True, required=False)
    back_shiny = serializers.URLField(allow_null=True, required=False)
    back_shiny_female = serializers.URLField(allow_null=True, required=False)


class SpritesSerializer(serializers.Serializer):
    back_default = serializers.URLField(allow_null=True)
    back_female = serializers.URLField(allow_null=True)
    back_shiny = serializers.URLField(allow_null=True)
    back_shiny_female = serializers.URLField(allow_null=True)
    front_default = serializers.URLField(allow_null=True)
    front_female = serializers.URLField(allow_null=True)
    front_shiny = serializers.URLField(allow_null=True)
    front_shiny_female = serializers.URLField(allow_null=True)


class TypeSerializer(serializers.Serializer):
    name = serializers.CharField(source='type.name', max_length=100)


class PokedexPokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    moves = PokemonMoveSerializer(many=True)
    sprites = SpritesSerializer()
    types = TypeSerializer(many=True)

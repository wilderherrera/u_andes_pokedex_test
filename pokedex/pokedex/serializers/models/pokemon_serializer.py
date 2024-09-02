from rest_framework import serializers

from pokedex.models import Pokemon, Move, Type, Sprite, PokemonMove, PokemonType, PokemonSprite


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['name']


class PokemonMoveSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='move.name')

    class Meta:
        model = PokemonMove
        fields = ['name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


class PokemonTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='type.name')

    class Meta:
        model = PokemonType
        fields = ['name']


class SpriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprite
        fields = [
            'back_default', 'back_female', 'back_shiny', 'back_shiny_female',
            'front_default', 'front_female', 'front_shiny', 'front_shiny_female'
        ]


class PokemonSpriteSerializer(serializers.ModelSerializer):
    sprite = SpriteSerializer()

    class Meta:
        model = PokemonSprite
        fields = ['sprite']


class PokemonSerializer(serializers.ModelSerializer):
    moves = PokemonMoveSerializer(source='pokemonmove_set', many=True)
    types = PokemonTypeSerializer(source='pokemontype_set', many=True)
    sprites = PokemonSpriteSerializer(source='pokemonsprite_set', many=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'moves', 'types', 'sprites']

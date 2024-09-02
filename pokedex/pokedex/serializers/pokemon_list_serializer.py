from rest_framework import serializers


class PokemonListSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.CharField()


class PokemonDataSerializer(serializers.Serializer):
    results = PokemonListSerializer(many=True)
    count = serializers.IntegerField()
    next = serializers.CharField()
    previous = serializers.CharField()

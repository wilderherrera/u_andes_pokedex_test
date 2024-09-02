from pokedex.models import Pokemon, Move, PokemonMove, Sprite, PokemonSprite, Type, PokemonType


class PokemonRepository:
    def exists_by_id(self, pokemon_id: int) -> bool:
        return Pokemon.objects.filter(id=pokemon_id).exists()

    def create_pokemon_with_details(self, data):
        pokemon, created = Pokemon.objects.get_or_create(
            id=data['id'],
            defaults={'name': data['name']}
        )

        for move_data in data['moves']:
            move, _ = Move.objects.get_or_create(name=move_data['name'])
            PokemonMove.objects.get_or_create(pokemon=pokemon, move=move)

        sprite_data = data['sprites']
        sprite, _ = Sprite.objects.get_or_create(
            back_default=sprite_data['back_default'],
            back_female=sprite_data.get('back_female', ''),
            back_shiny=sprite_data['back_shiny'],
            back_shiny_female=sprite_data.get('back_shiny_female', ''),
            front_default=sprite_data['front_default'],
            front_female=sprite_data.get('front_female', ''),
            front_shiny=sprite_data['front_shiny'],
            front_shiny_female=sprite_data.get('front_shiny_female', '')
        )
        PokemonSprite.objects.get_or_create(pokemon=pokemon, sprite=sprite)

        for type_data in data['types']:
            type_instance, _ = Type.objects.get_or_create(name=type_data['name'])
            PokemonType.objects.get_or_create(pokemon=pokemon, type=type_instance)

        return pokemon

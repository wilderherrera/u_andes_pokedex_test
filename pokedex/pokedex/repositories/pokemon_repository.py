from pokedex.models import Pokemon, Move, PokemonMove, Sprite, PokemonSprite, Type, PokemonType
from pokedex.serializers.pokedex_pokemon_serializer import PokedexPokemonSerializer


class PokemonRepository:
    """
    A repository class for managing the persistence and retrieval of Pokémon-related data.

    This class provides methods to fetch, create, update, and check the existence of Pokémon,
    along with their associated moves, sprites, and types.
    """

    def get_by_id_or_name(self, pokemon_id_or_name):
        """
        Retrieves a Pokémon by its ID or name.

        Args:
            pokemon_id_or_name (int or str): The ID or name of the Pokémon to retrieve.

        Returns:
            Pokemon: A Pokemon object.

        Raises:
            Pokemon.DoesNotExist: If no Pokémon with the given ID or name exists.
        """
        if str(pokemon_id_or_name).isdigit():
            return Pokemon.objects.get(id=int(pokemon_id_or_name))
        else:
            return Pokemon.objects.get(name=pokemon_id_or_name)

    def exists_by_id(self, pokemon_id: int) -> bool:
        """
        Checks if a Pokémon exists by its ID.

        Args:
            pokemon_id (int): The ID of the Pokémon to check.

        Returns:
            bool: True if the Pokémon exists, False otherwise.
        """
        return Pokemon.objects.filter(id=pokemon_id).exists()

    def exists_by_name(self, pokemon_name: str) -> bool:
        """
        Checks if a Pokémon exists by its name.

        Args:
            pokemon_name (str): The name of the Pokémon to check.

        Returns:
            bool: True if the Pokémon exists, False otherwise.
        """
        return Pokemon.objects.filter(name=pokemon_name).exists()

    def create_pokemon_with_details(self, data: PokedexPokemonSerializer):
        """
        Creates a Pokémon and its associated details (moves, sprites, types) in the database.

        Args:
            data (dict): A dictionary containing Pokémon data, including moves, sprites, and types.

        Returns:
            Pokemon: The created or retrieved Pokemon object.
        """
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

    def update(self, pokemon_id, data):
        """
        Updates an existing Pokémon's details in the database.

        Args:
            pokemon_id (int or str): The ID or name of the Pokémon to update.
            data (dict): A dictionary containing the updated Pokémon data.

        Returns:
            Pokemon: The updated Pokemon object.

        Raises:
            ValueError: If the Pokémon with the given ID or name does not exist.
        """
        try:
            pokemon = self.get_by_id_or_name(pokemon_id)
        except Pokemon.DoesNotExist:
            raise ValueError(f"Pokemon with id or name '{pokemon_id}' does not exist.")

        if 'name' in data:
            pokemon.name = data['name']
            pokemon.save()

        if 'moves' in data:
            self._update_moves(pokemon, data['moves'])

        if 'sprites' in data:
            self._update_sprites(pokemon, data['sprites'])

        if 'types' in data:
            self._update_types(pokemon, data['types'])

        return pokemon

    def _update_moves(self, pokemon, moves_data):
        """
        Updates the moves associated with a Pokémon.

        Args:
            pokemon (Pokemon): The Pokemon object to update.
            moves_data (list): A list of move data to update.
        """
        existing_moves = set(PokemonMove.objects.filter(pokemon=pokemon).values_list('move__name', flat=True))
        new_moves = set(move_data['name'] for move_data in moves_data)

        moves_to_remove = existing_moves - new_moves
        PokemonMove.objects.filter(pokemon=pokemon, move__name__in=moves_to_remove).delete()

        for move_name in new_moves - existing_moves:
            move, _ = Move.objects.get_or_create(name=move_name)
            PokemonMove.objects.get_or_create(pokemon=pokemon, move=move)

    def _update_sprites(self, pokemon, sprites_data):
        """
        Updates the sprites associated with a Pokémon.

        Args:
            pokemon (Pokemon): The Pokemon object to update.
            sprites_data (list): A list of sprite data to update.
        """
        PokemonSprite.objects.filter(pokemon=pokemon).delete()

        for sprite_data in sprites_data:
            sprite_info = sprite_data['sprite']
            sprite, _ = Sprite.objects.get_or_create(
                back_default=sprite_info.get('back_default', ''),
                back_female=sprite_info.get('back_female', ''),
                back_shiny=sprite_info.get('back_shiny', ''),
                back_shiny_female=sprite_info.get('back_shiny_female', ''),
                front_default=sprite_info.get('front_default', ''),
                front_female=sprite_info.get('front_female', ''),
                front_shiny=sprite_info.get('front_shiny', ''),
                front_shiny_female=sprite_info.get('front_shiny_female', '')
            )
            PokemonSprite.objects.create(pokemon=pokemon, sprite=sprite)

    def _update_types(self, pokemon, types_data):
        """
        Updates the types associated with a Pokémon.

        Args:
            pokemon (Pokemon): The Pokemon object to update.
            types_data (list): A list of type data to update.
        """
        existing_types = set(PokemonType.objects.filter(pokemon=pokemon).values_list('type__name', flat=True))
        new_types = set(type_data['name'] for type_data in types_data)

        types_to_remove = existing_types - new_types
        PokemonType.objects.filter(pokemon=pokemon, type__name__in=types_to_remove).delete()

        for type_name in new_types - existing_types:
            type_instance, _ = Type.objects.get_or_create(name=type_name)
            PokemonType.objects.get_or_create(pokemon=pokemon, type=type_instance)

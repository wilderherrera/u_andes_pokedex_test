from pokedex.repositories.pokemon_repository import PokemonRepository


class PokemonService:
    """
    A service class that provides business logic for handling Pokémon data.

    This service acts as a layer between the API views and the repository,
    managing the retrieval and updating of Pokémon data.
    """

    def __init__(self):
        """
        Initializes the PokemonService with a PokemonRepository instance.
        """
        self.pokemon_repository = PokemonRepository()

    def get_by_id_or_name(self, pokemon_id):
        """
        Retrieves a Pokémon by its ID or name.

        Args:
            pokemon_id (int or str): The ID or name of the Pokémon to retrieve.

        Returns:
            Pokemon: A Pokemon object retrieved from the repository.

        Raises:
            Pokemon.DoesNotExist: If no Pokémon with the given ID or name exists.
        """
        return self.pokemon_repository.get_by_id_or_name(pokemon_id)

    def update_pokemon(self, pokemon_id, data):
        """
        Updates a Pokémon's details in the repository.

        Args:
            pokemon_id (int or str): The ID or name of the Pokémon to update.
            data (dict): A dictionary containing the updated Pokémon data.

        Returns:
            Pokemon: The updated Pokémon object.

        Raises:
            Pokemon.DoesNotExist: If no Pokémon with the given ID or name exists.
        """
        return self.pokemon_repository.update(pokemon_id, data)

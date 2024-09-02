from pokedex.repositories.pokemon_repository import PokemonRepository


class PokemonService:
    def __init__(self):
        self.pokemon_repository = PokemonRepository()

    def get_by_id_or_name(self, pokemon_id):
        return self.pokemon_repository.get_by_id_or_name(pokemon_id)

    def update_pokemon(self, pokemon_id, data):
        return self.pokemon_repository.update(pokemon_id, data)

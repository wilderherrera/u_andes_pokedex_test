from django.test import TestCase

from pokedex.models import Pokemon, Move, PokemonMove, Sprite, PokemonSprite, Type, PokemonType
from pokedex.repositories.pokemon_repository import PokemonRepository


class PokemonRepositoryTest(TestCase):
    def setUp(self):
        self.pokemon_repository = PokemonRepository()
        self.pokemon = Pokemon.objects.create(id=1, name="Bulbasaur")
        self.move1 = Move.objects.create(name="Tackle")
        self.move2 = Move.objects.create(name="Growl")
        self.type1 = Type.objects.create(name="Grass")
        self.type2 = Type.objects.create(name="Poison")
        self.sprite = Sprite.objects.create(
            back_default="back_default_url",
            back_female="",
            back_shiny="back_shiny_url",
            back_shiny_female="",
            front_default="front_default_url",
            front_female="",
            front_shiny="front_shiny_url",
            front_shiny_female=""
        )
        PokemonMove.objects.create(pokemon=self.pokemon, move=self.move1)
        PokemonType.objects.create(pokemon=self.pokemon, type=self.type1)
        PokemonSprite.objects.create(pokemon=self.pokemon, sprite=self.sprite)

    def test_get_by_id_or_name(self):
        pokemon = self.pokemon_repository.get_by_id_or_name(1)
        self.assertEqual(pokemon.name, "Bulbasaur")

        pokemon = self.pokemon_repository.get_by_id_or_name("Bulbasaur")
        self.assertEqual(pokemon.id, 1)

    def test_exists_by_id(self):
        self.assertTrue(self.pokemon_repository.exists_by_id(1))
        self.assertFalse(self.pokemon_repository.exists_by_id(999))

    def test_exists_by_name(self):
        self.assertTrue(self.pokemon_repository.exists_by_name("Bulbasaur"))
        self.assertFalse(self.pokemon_repository.exists_by_name("Pikachu"))

    def test_create_pokemon_with_details(self):
        data = {
            "id": 2,
            "name": "Ivysaur",
            "moves": [
                {"name": "Vine Whip"},
                {"name": "Tackle"}
            ],
            "sprites":
                {
                    "back_default": "back_default_ivysaur",
                    "back_female": "",
                    "back_shiny": "back_shiny_ivysaur",
                    "back_shiny_female": "",
                    "front_default": "front_default_ivysaur",
                    "front_female": "",
                    "front_shiny": "front_shiny_ivysaur",
                    "front_shiny_female": ""
                }
            ,
            "types": [
                {"name": "Grass"},
                {"name": "Poison"}
            ]
        }

        pokemon = self.pokemon_repository.create_pokemon_with_details(data)
        self.assertEqual(pokemon.id, 2)
        self.assertEqual(pokemon.name, "Ivysaur")
        self.assertEqual(PokemonSprite.objects.filter(pokemon=pokemon).count(), 1)

    def test_update_pokemon(self):
        update_data = {
            "name": "Bulbasaur Updated",
            "moves": [
                {"name": "Vine Whip"},
                {"name": "Growl"}
            ],
            "sprites": [
                {
                    "sprite": {
                        "back_default": "new_back_default_url",
                        "back_female": "",
                        "back_shiny": "new_back_shiny_url",
                        "back_shiny_female": "",
                        "front_default": "new_front_default_url",
                        "front_female": "",
                        "front_shiny": "new_front_shiny_url",
                        "front_shiny_female": ""
                    }
                }
            ],
            "types": [
                {"name": "Grass"},
                {"name": "Poison"}
            ]
        }

        updated_pokemon = self.pokemon_repository.update(1, update_data)
        self.assertEqual(updated_pokemon.name, "Bulbasaur Updated")
        self.assertTrue(PokemonMove.objects.filter(pokemon=updated_pokemon, move__name="Vine Whip").exists())

        self.assertFalse(PokemonMove.objects.filter(pokemon=updated_pokemon, move__name="Tackle").exists())

        self.assertEqual(PokemonSprite.objects.filter(pokemon=updated_pokemon).count(), 1)
        sprite = PokemonSprite.objects.get(pokemon=updated_pokemon)
        self.assertEqual(sprite.sprite.back_default, "new_back_default_url")

        self.assertTrue(PokemonType.objects.filter(pokemon=updated_pokemon, type__name="Grass").exists())
        self.assertTrue(PokemonType.objects.filter(pokemon=updated_pokemon, type__name="Poison").exists())

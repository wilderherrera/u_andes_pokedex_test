from django.db import models


class PokemonSprite(models.Model):
    pokemon = models.ForeignKey('pokedex.Pokemon', on_delete=models.CASCADE, db_column='pokemon_id')
    sprite = models.ForeignKey('pokedex.Sprite', on_delete=models.CASCADE, db_column='sprite_id')

    class Meta:
        db_table = 'pokemon_sprites'
        unique_together = ('pokemon', 'sprite')

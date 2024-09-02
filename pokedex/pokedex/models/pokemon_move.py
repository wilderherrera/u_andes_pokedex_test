from django.db import models


class PokemonMove(models.Model):
    pokemon = models.ForeignKey('pokedex.Pokemon', on_delete=models.CASCADE, db_column='pokemon_id')
    move = models.ForeignKey('pokedex.Move', on_delete=models.CASCADE, db_column='move_id')

    class Meta:
        db_table = 'pokemon_moves'
        unique_together = ('pokemon', 'move')

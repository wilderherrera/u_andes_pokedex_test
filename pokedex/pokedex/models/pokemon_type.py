from django.db import models


class PokemonType(models.Model):
    pokemon = models.ForeignKey('pokedex.Pokemon', on_delete=models.CASCADE, db_column='pokemon_id')
    type = models.ForeignKey('pokedex.Type', on_delete=models.CASCADE, db_column='type_id')

    class Meta:
        db_table = 'pokemon_types'
        unique_together = ('pokemon', 'type')

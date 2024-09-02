from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    
    class Meta:
        db_table = 'pokemons'

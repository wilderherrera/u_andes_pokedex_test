from django.db import models


class Move(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'moves'

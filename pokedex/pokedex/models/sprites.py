from django.db import models


class Sprite(models.Model):
    back_default = models.CharField(max_length=100, null=True)
    back_female = models.CharField(max_length=100, null=True)
    back_shiny = models.CharField(max_length=100, null=True)
    back_shiny_female = models.CharField(max_length=100, null=True)
    front_default = models.CharField(max_length=100, null=True)
    front_female = models.CharField(max_length=100, null=True)
    front_shiny = models.CharField(max_length=100, null=True)
    front_shiny_female = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'sprites'

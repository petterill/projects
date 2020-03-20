from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    overall_rank = models.IntegerField()
    score = models.FloatField()
    gdp_per_capita = models.FloatField()
    social_support = models.FloatField()
    healthy_life_expectancy = models.FloatField()
    freedom_to_make_life_choices = models.FloatField()
    generosity = models.FloatField()
    perceptions_of_corruption = models.FloatField()

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = (
            "id",
            "url",
            "name",
            "overall_rank",
            "score",
            "gdp_per_capita",
            "social_support",
            "healthy_life_expectancy",
            "freedom_to_make_life_choices",
            "generosity",
            "perceptions_of_corruption",
        )

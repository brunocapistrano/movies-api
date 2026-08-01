from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Movie
        fields = '__all__'


    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo não pode conter mais de 200 caracteres.')


    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None
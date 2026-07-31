from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = '__all__'

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo não pode conter mais de 200 caracteres.')
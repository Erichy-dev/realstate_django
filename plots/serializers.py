from rest_framework import serializers

from .models import Plot, PlotPic, PlotOccupant

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = (
            '__all__'
        )

class PlotPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotPic
        fields = (
            '__all__'
        )

class PlotOccupantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotOccupant
        fields = (
            '__all__'
        )

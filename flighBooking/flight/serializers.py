from rest_framework import serializers
from flight.models import Flight, Passenger, Reservation
import re


class Flightserializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validated_fightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$", flightNumber) == None):
            raise serializers.ValidationError("invalid flight number")
        return flightNumber


class Passengerserializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

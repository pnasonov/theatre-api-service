from django.db import transaction
from rest_framework import serializers

from theatre.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class PlaySerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=False)
    genres = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Play
        fields = "__all__"

    def create(self, validated_data):
        actors_data = validated_data.pop("actors")
        genres_data = validated_data.pop("genres")
        play = Play.objects.create(**validated_data)
        for actor_data in actors_data:
            play.actors.add(Actor.objects.create(**actor_data))
        for genre_data in genres_data:
            play.genres.add(Genre.objects.create(**genre_data))
        return play


class TheatreHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheatreHall
        fields = "__all__"


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer(read_only=True)
    theatre_hall = TheatreHallSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance")


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False)

    class Meta:
        model = Reservation
        fields = ("id", "tickets", "created_at")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            reservation = Reservation.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)
            return reservation

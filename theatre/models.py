from django.conf import settings
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True, related_name="plays")
    genres = models.ManyToManyField(Genre, blank=True, related_name="plays")

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class TheatreHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(
        Play, on_delete=models.CASCADE, related_name="performances"
    )
    theatre_hall = models.ForeignKey(
        TheatreHall, on_delete=models.CASCADE, related_name="performances"
    )
    show_time = models.DateTimeField()

    class Meta:
        ordering = ["-show_time"]

    def __str__(self) -> str:
        return f"{self.play} - {self.theatre_hall} at {self.show_time}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user} at {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(
        Performance, on_delete=models.CASCADE, related_name="tickets"
    )
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="tickets"
    )

    class Meta:
        ordering = ["row", "seat"]

    def __str__(self) -> str:
        return f"{self.performance} row: {self.row} seat: {self.seat}"

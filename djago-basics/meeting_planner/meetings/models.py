from datetime import time
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} at {self.floor_number} on {self.room_number}"


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


class Agenda(models.Model):
    title = models.CharField(max_length=500)
    ordinal_num = models.IntegerField()
    start_time = models.TimeField(default=time(9))
    end_time = models.TimeField(default=time(9))
    meeting = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.ordinal_num}. {self.start_time} - {self.end_time} {self.title}"

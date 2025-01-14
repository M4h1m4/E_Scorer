from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    # performers = models.ManyToManyField('Performer')

class Performer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    performance_time_limit = models.IntegerField(default=2)

class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

class Score(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    timestamp = models.DateTimeField(auto_now_add=True)


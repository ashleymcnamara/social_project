from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LIST(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.CharField(max_length=500, null=True, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='user')
    updated = models.DateTimeField(auto_now=True)
    time = models.IntegerField(verbose_name='Time')
    completed = models.NullBooleanField()


    def print_time(self):
        minutes = self.time
        minutes_in_day = 1440
        minutes_in_hour = 60
        days = 0
        hours = 0
        while minutes >= minutes_in_day:
            days += 1
            minutes -= minutes_in_day
        while minutes >= minutes_in_hour:
            hours += 1
            minutes -= minutes_in_hour
        timestr = ""
        if days!=0:
            timestr = timestr +str(days) + "d "
        if hours!=0:
            timestr = timestr +str(hours) + "h "
        if minutes!=0:
            timestr = timestr +str(minutes) + "m"
        return  timestr


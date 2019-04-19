from __future__ import unicode_literals
from django.db import models
from apps.log_app.models import User
import datetime
import re

class TripManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        todaydate = datetime.date.today()
        start = postData['start']
        if len(postData['dest']) < 3:
            errors["dest"] = "Destination should be at least 3 characters"
        if len(postData['start']) < 10:
            errors["start"] = "Please select a date"
        elif str(start) < str(todaydate):
            errors["start"] = "You cannot time travel, sorry :("
        if len(postData['end']) < 10:
            errors["end"] = "Please select a date"
        elif postData['end'] < postData['start']:
            errors["late"] = "Your end date can't be after you start"
        if len(postData['plan']) < 3:
            errors["plan"] = "Plan should be at least 3 characters"
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=45)
    start = models.DateField()
    end = models.DateField()
    plan = models.TextField()
    host = models.ForeignKey(User, related_name="trip", null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(User, related_name="trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
    def __repr__(self):
        return f"Trip: {self.destination}"
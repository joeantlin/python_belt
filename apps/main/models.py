from __future__ import unicode_literals
from django.db import models
from apps.log_app.models import User

class EventManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        pass
        return errors

class Event(models.Model):
    pass
    objects = EventManager()
    def __repr__(self):
        return f"Event: {self.name}"
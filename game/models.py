from django.db import models
from django.contrib.auth.models import User as U


# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=30)
    online = models.BooleanField(default = U.is_active)

    def __str__(self):
        return self.nickname

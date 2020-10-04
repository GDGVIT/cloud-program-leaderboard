from django.db import models
from uuid import uuid4
# Create your models here.
class UserModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    qwiklabs_id = models.CharField(max_length=300)
    quests_status = models.IntegerField()
    quests = models.JSONField()
    dp = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
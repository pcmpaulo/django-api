import uuid
from datetime import datetime

from django.db import models

class User(models.Model):
    id = models.UUIDField(auto_created=True,primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_created=True, default=datetime.now)

    class Meta:
        db_table = 'USER'

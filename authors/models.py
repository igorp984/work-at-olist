from django.db import models
import uuid


# Create your models here.


class Authors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Author", max_length=300)

    def __str__(self):
        return self.name

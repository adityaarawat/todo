from django.db import models

# Create your models here.

class Tasks(models.Model):
    task=models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)
    created_at=models.BooleanField(default=True)
    updated_at=models.BooleanField(default=True)

    def __str__(self):
        return self.task

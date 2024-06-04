from django.conf import settings
from django.db import models
import datetime

class TodoItem(models.Model):
    created_at = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return f'  ({self.id})  {self.title}'

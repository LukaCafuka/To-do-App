from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    completed = models.BooleanField(default='False')

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.text

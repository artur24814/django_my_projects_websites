from django.db import models
from django.contrib.auth.models import User

class Words(models.Model):
    word = models.CharField(max_length=260)
    definition = models.CharField(max_length=260)
    data = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    alphabet = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.alphabet = self.word[0]
        super().save(*args, **kwargs)



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

    def get_absolute_url(self):
        return f'/update_word/{self.id}/'
    def __str__(self):
        return self.definition

class TextWithWord(models.Model):
    word = models.ForeignKey('Words', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    no_of_likes = models.IntegerField(default=0)

class LikeText(models.Model):
    text = models.ForeignKey('TextWithWord', on_delete=models.CASCADE)
    username = models.CharField(max_length=64)

class CommentsText(models.Model):
    text = models.CharField(max_length=350)
    post = models.ForeignKey('TextWithWord', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class CommentsToComents(models.Model):
    comment = models.ForeignKey('CommentsText', on_delete=models.CASCADE)
    author = models.CharField(max_length=64)

class RandomWordForHomeView(models.Model):
    word = models.ForeignKey('Words', on_delete=models.DO_NOTHING, null=True)



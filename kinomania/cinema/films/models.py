from django.db import models
from django.shortcuts import redirect

columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rows = ['a', 'b', 'c', 'd','e']
rowcolums_set = []
for letter in rows:
    for index in columns:
        rowcolums_set.append(letter+str(index))


class Film(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    in_cinema = models.DateField()

    def __str__(self):
        return self.title

class Hall(models.Model):
    title = models.CharField(max_length=64)
    used_to = models.DateField(null=True)
    changed = models.DateField(auto_now=True)
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return f'/hall/{self.id}'

class Screening(models.Model):
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, blank=True)
    time = models.CharField(max_length=28)

    def get_url(self):
        return f'/{self.id}/{self.hall}/{self.time}/'

    def save(self, *args, **kwargs):
        self.hall = Hall.objects.get(film= self.film)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.film

class Ticket(models.Model):
    screening = models.ForeignKey('Screening', on_delete=models.CASCADE)
    rowcolums = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        if self.rowcolums in rowcolums_set:
            super().save(*args,**kwargs)
        else:
            return redirect("/Error/")


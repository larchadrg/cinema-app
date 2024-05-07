from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    #min_age
    #genre 

class CinemaFunction(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #TODO: in case of cancellation, notify the clients 
    date = models.DateTimeField()

class Viewer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cinema_function = models.ForeignKey(CinemaFunction, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
class Experience(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class LocationOfWork(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    subtitle = models.CharField(max_length=200)
    location = models.ManyToManyField(LocationOfWork)

    def __str__(self):
        return self.subtitle

from django.db import models

# Create your models here.
class Experience(models.Model):
    name = models.CharField(max_length=200, Unique=True)
    id = models.AutoField(primary_key=True)

class Vacancy(models.Model):
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

class LocationOfWork(models.Model):
    name = models.CharField(max_length=200, Unique=True)
    id = models.AutoField(primary_key=True)

class VacancyLocation(models.Model):
    location_id = models.ForeignKey(LocationOfWork, on_delete=models.CASCADE)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
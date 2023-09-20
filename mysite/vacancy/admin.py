from django.contrib import admin

# Register your models here.
from .models import Vacancy
from .models import Experience
from .models import LocationOfWork
from .models import VacancyLocation

admin.site.register(Vacancy)
admin.site.register(Experience)
admin.site.register(LocationOfWork)
admin.site.register(VacancyLocation)
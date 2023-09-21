from django.contrib import admin

# Register your models here.
from .models import Vacancy
from .models import Vacancy
from .models import LocationOfWork
from .models import Experience

admin.site.register(Vacancy)
admin.site.register(LocationOfWork)
admin.site.register(Experience)
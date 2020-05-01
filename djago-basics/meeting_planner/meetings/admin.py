from django.contrib import admin

from .models import Meeting
from .models import Agenda
from .models import Room

admin.site.register(Meeting)
admin.site.register(Agenda)
admin.site.register(Room)


from django.contrib import admin
from .models import (
     Player,
)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
     list_display_links = ('first_name', 'middle_name', 'last_name')
     list_display = ('first_name','middle_name', 'last_name', 'position', 'pom', 'captain')
     fields = (
          ('first_name','middle_name', 'last_name',),
          ('_dob', 'position',),
          'bio', 'profile_pic', 'captain', 'pom',
     )

     list_filter = ('position', 'captain',)

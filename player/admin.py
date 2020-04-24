from django.contrib import admin
from .models import (
     Player,
     Pom
)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
     list_display_links = ('first_name', 'middle_name', 'last_name')
     list_display = ('first_name','middle_name', 'last_name', 'position', 'pom')
     fields = (
          ('first_name','middle_name', 'last_name',),
          ('_dob', 'position',),
          'bio', 'profile_pic',
     )

admin.site.register(Pom)
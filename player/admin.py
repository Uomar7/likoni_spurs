from django.contrib import admin
from .models import (
     Player,
     Pom
)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
     list_display_links = ('first_name', 'middle_name', 'last_name')
     list_display = ('first_name','middle_name', 'last_name', 'position')
     fields = (
          ('first_name','middle_name', 'last_name',),
          ('dob', 'position',),
          'bio',
     )

admin.site.register(Pom)
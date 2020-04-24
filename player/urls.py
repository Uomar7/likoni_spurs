from django.urls import path
from .views import (
     PlayersList,
)

urlpatterns = [
     path('players/',PlayersList.as_view(), name='home'),
]
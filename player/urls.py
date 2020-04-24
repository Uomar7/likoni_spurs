from django.urls import path
from .views import (
     PlayersList,
     PlayerDetail,
)

urlpatterns = [
     path('players/',PlayersList.as_view(), name='player_list'),
     path('player_detail/<int:pk>/', PlayerDetail.as_view(), name='detail'),
]
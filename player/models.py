from django.db import models
import datetime as dt

class Player(models.Model):

     POSITIONS = (
          ('GK', 'Goalkeeper'),
          ('CB', 'Center Back'),
          ('LB', 'Left Back'),
          ('RB', 'Right Back'),
          ('CM', 'Center Midfield'),
          ('AM', 'Attacking Midfield'),
          ('CF', 'Center Forward'),
          ('ST', 'Striker'),
     )

     profile_pic = models.ImageField("Player's image", upload_to='profiles/', blank=True)
     first_name = models.CharField('First name', max_length=50)
     middle_name = models.CharField('Middle name', max_length=50, blank=True)
     last_name = models.CharField('Last name', max_length=50)
     _dob = models.DateField('Date of Birth')
     captain = models.BooleanField('Captain', default=False)
     pom = models.BooleanField('Player of the month', default=False)
     position = models.CharField("Player position",choices=POSITIONS, default="Choose position", max_length=50)
     bio = models.TextField("Player's Biography", blank=True)

     def __str__(self):
          return self.first_name +" "+ self.middle_name +" "+ self.last_name
     
     def get_date_of_birth(self):
          return self._dob

from django.db import models

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

     profile_pic = models.ImageField("Player's image", upload_to='profiles/')
     first_name = models.CharField('First name', max_length=50)
     middle_name = models.CharField('Middle name', max_length=50)
     last_name = models.CharField('Last name', max_length=50)
     dob = models.DateField('Date of Birth')
     position = models.CharField("Player position",choices=POSITIONS, default="Choose position", max_length=50)
     bio = models.TextField("Player's Biography", blank=True)

     def __str__(self):
          return self.first_name +" "+ self.last_name

class Pom(models.Model):
     player = models.OneToOneField(Player, on_delete=models.CASCADE)

     def __str__(self):
          return self.player.first_name
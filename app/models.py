from django.db import models

# Create your models here.
class Ipl(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.ForeignKey(Ipl,on_delete=models.CASCADE)
    player=models.CharField(max_length=100)
    captain=models.CharField(max_length=100)
    def __str__(self):
        return self.player


class Record(models.Model):
    name=models.ForeignKey(Team,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.name
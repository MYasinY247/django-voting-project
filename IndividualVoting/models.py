from django.db import models
# Authorship Muhammad Yasin Yahya W1974891
# Create your models here.
class Feedback(models.Model):
    session=models.CharField(max_length=100,db_column='5CS01_01_G_Session')
    emotion=models.CharField(max_length=100,db_column='5CS01_01_G_Vote')
    team=models.CharField(max_length=100,db_column='5CS01_01_G_Team')


    def __str__(self):
        return "Session: " +str(self.session) + "| Vote: "+ self.emotion + "| Team: " +str(self.team)
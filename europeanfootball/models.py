from django.db import models
from django.contrib.postgres.fields import ArrayField

class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=255)
    class Meta:
        db_table = "lountry"

class League(models.Model):
    league_id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Country,on_delete = models.CASCADE)
    league_name = models.CharField(max_length=255)
    class Meta:
        db_table = "league"
    def __str__(self):
        return str(self.league_id)

class Team(models.Model):
    team_id= models.IntegerField(primary_key=True)
    team_short_name = models.CharField(max_length=255)
    team_long_name = models.CharField(max_length=255)
    league = models.ForeignKey(League,on_delete = models.CASCADE)  
    class Meta:
        db_table = "team"  
    def __str__(self):
        return str(self.team_id)

class Matchstats(models.Model):
    id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League,on_delete = models.CASCADE)
    season = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    home_team_id = models.IntegerField()
    away_team_id = models.IntegerField()
    home_team_goal = models.IntegerField()
    away_team_goal = models.IntegerField()
    goals_info = ArrayField(ArrayField(models.CharField(max_length =255)))
    card_info = ArrayField(ArrayField(models.TextField()))
    corner_info = ArrayField(ArrayField(models.TextField()))

    class Meta:
        db_table = "matchstats"

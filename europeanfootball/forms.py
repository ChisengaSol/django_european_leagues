from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import Matchstats

class MatchDetailsForm(forms.ModelForm):
    class Meta:
        model = Matchstats
        #fields = ["Home_Team", "Home_team_goal","Away_Team_goal", "Away_Team"]
        fields = ('league','date','home_team_id','home_team_goal','away_team_id','away_team_goal')
        labels = {
            'league': 'League ID',
            'date': 'Date(e.g 20/12/2015 00:00)',
            'home_team_id': 'Home Team ID',
            'home_team_goal': 'Home Team Score',
            'away_team_id': 'Away Team ID',
            'away_team_goal': 'Away Team Score'
        }
    def __init__(self,*args,**kwargs):
        super(MatchDetailsForm, self).__init__(*args,**kwargs)
        self.fields['league'].empty_label = "Select"

        

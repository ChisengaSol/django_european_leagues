from django.shortcuts import render, HttpResponseRedirect
from .models import Matchstats
from .forms import MatchDetailsForm
from datetime import datetime

def matchstat_list(req):
    #results = Matchstats.objects.all()
    #return render(req, "europeanfootball/matchstat_list.html",{'data':results})
    return 

def matchstat_form(req):
    '''
        Function displays records and adds records to the database
        ('league','home_team_id','home_team_goal','away_team_id','away_team_goal')
        now.strftime("%d/%m/%Y %H:%M:%S")
    '''
    if req.method == "POST":
        form = MatchDetailsForm(req.POST)
        if form.is_valid():
            leag = form.cleaned_data['league']
            dte = form.cleaned_data['date']
            home_id = form.cleaned_data['home_team_id']
            home_goal = form.cleaned_data['home_team_goal']
            away_id = form.cleaned_data['away_team_id']
            away_goal = form.cleaned_data['away_team_goal']
            cleaned_stats = Matchstats(league = leag, date = dte,home_team_id = home_id, 
                                        home_team_goal = home_goal,away_team_id = away_id,away_team_goal = away_goal)            
            cleaned_stats.save()
            form = MatchDetailsForm()

    else:
        form = MatchDetailsForm()
    results = Matchstats.objects.all()
    return render(req,"europeanfootball/matchstat_form.html", {'form':form,'data':results})

def matchstat_del(req, id):
    """Function to delete record from database"""
    if req.method == "POST":
        pi = Matchstats.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/eurofootball/')

def update_matchstats(req,id):
    if req.method == "POST":
        pi = Matchstats.objects.get(pk = id)
        form = MatchDetailsForm(req.POST, instance = pi)
        if form.is_valid():
            form.save()
    else:
        pi = Matchstats.objects.get(pk = id)
        form = MatchDetailsForm(instance = pi)
    return render(req, "europeanfootball/update_matchstats.html",{'form':form})
    


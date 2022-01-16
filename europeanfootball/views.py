from urllib import request
from django.shortcuts import render, HttpResponseRedirect
from .models import Matchstats, Team
from .forms import MatchDetailsForm

#things for pagination
from django.core.paginator import Paginator

def matchstat_form(req):
    """
        Function displays records and adds records to the database
    """
    #pagination setup
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
    results = Matchstats.objects.all().order_by('-id')
    p = Paginator(results,15)
    page = req.GET.get('page')
    matches = p.get_page(page)
    team_info = Team.objects.all().values('team_id','team_long_name')    
    return render(req,"europeanfootball/matchstat_form.html", {'form':form,'data':results, 'matches':matches,'team_info':team_info})

def matchstat_del(req, id):
    """Function to delete record from database"""
    if req.method == "POST":
        match = Matchstats.objects.get(pk = id)
        match.delete()
        return HttpResponseRedirect('/eurofootball/')

def update_matchstats(req,id):
    """Update records  in the DB"""
    if req.method == "POST":
        match = Matchstats.objects.get(pk = id)
        form = MatchDetailsForm(req.POST, instance = match)
        if form.is_valid():
            form.save()
    else:
        match = Matchstats.objects.get(pk = id)
        form = MatchDetailsForm(instance = match)
    return render(req, "europeanfootball/update_matchstats.html",{'form':form})
    


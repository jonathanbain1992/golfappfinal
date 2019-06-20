# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext
from ip2app.models import TeamTournament, GolfTeam, GolfPlayer


from django.http import HttpResponse
from django.views import View
from ip2app.forms import TeamTournamentForm, GolfTeamForm

# Create your views here.
def Index(View):
    info = 'bla bla bla'
    context_dict = {'boldmsg': "i am a bold message"}
    return render_to_response('index.html',context_dict)

def About(View):
    context = {"title": "About"}
    return render_to_response("about.html", context)

def SignInRegister(View):
    return render_to_response("maintenance.html", {})

def Profile(View):
    context = { "title": "Under construction"}
    return render_to_response("maintenance.html", context=context)

def ScoreBoard(View):
    return render_to_response("scoreboard.html", {})

def tournament(request, name):
    context = {}
    try:
        team_tournament = TeamTournament.objects.get(slug=name)
        context['team_tournament'] = team_tournament
    except:
        pass
    return render_to_response("tournament/tournament.html", context=context)

    
def tournament_list(request):
    context = {}
    try:
        team_tournaments = TeamTournament.objects.all().order_by(
            "-dateTimeStart"
        )
        context['team_tournaments'] = team_tournaments
    except:
        pass
    return render_to_response("tournament/tournamentlist.html", context)

def golf_team(request, name):
    context = {}
    try:
        team = GolfTeam.objects.get(slug=name)
        context['team'] = team
        members = GolfPlayer.objects.filter(golfTeam=team)
        context['members'] = members
    except:
        pass
    return render_to_response("team/golf_team.html", context)


def add_team(request):
    if request.method =="POST":
        form = GolfTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=True)
            return golf_team(request, form['teamName'])
        else:
            print(form.errors)
    else:
        form = GolfTeamForm()
    return render(request, 'team/add_team.html', {'form': form})


def add_tournament(request):
    if request.method == "POST":
        form_tournament = TeamTournamentForm(request.POST)
        if form_tournament.is_valid():
            form_tournament.dateTimeStart = None
            form_tournament.dateTimeFinish = None
            form_tournament.save()
            print("Success: tournament created!")
            return tournament_list(request)
        else:
            print(form_tournament.errors)
    else:
        form_tournament = TeamTournamentForm()
    return render(request, 'tournament/add_tournament.html', 
                    {
                        'form_tournament': form_tournament,
                    }
    )
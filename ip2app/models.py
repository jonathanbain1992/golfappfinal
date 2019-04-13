# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GolfClub(models.Model):
    clubName = models.CharField(max_length=200)
    clubName9 = models.CharField(max_length=200)
    clubEstablished = models.DateField(auto_now=False)
    def __str__(self):
        return self.clubName

class GolfCourse(models.Model):
    courseName = models.CharField(max_length=200)
    golfClub = models.ForeignKey('GolfClub', on_delete=models.CASCADE,)
    def __str__(self):
        return self.courseName

class CourseHole(models.Model):
    golfCourse = models.ForeignKey('GolfCourse', on_delete=models.CASCADE,)
    #-6 to 7 par
    PARneg6 = -6
    PARneg5 = -5
    PARneg4 = -4
    PARneg3 = -3
    PARneg2 = -2
    PARneg1 = -1
    PAR0 = 0
    PAR1 = 1
    PAR2 = 2
    PAR3 = 3
    PAR4 = 4
    PAR5 = 5
    PAR6 = 6
    PAR7 = 7

    CHOICES = ( (PARneg6, "-6"), (PARneg5,"-5"), (PARneg4,"-4"),(PARneg3,"-3"),(PARneg2,"-2"),(PARneg1,"-1"),(PAR0,"0"),(PAR1,"1"),(PAR2,"2"),
    (PAR3,"3"),(PAR4,"4"),(PAR5,"5"),(PAR6,"6"),(PAR7,"7"),)
    holeName = models.CharField(max_length=200)
    holePar = models.IntegerField(choices= CHOICES,default=PAR0)

    def __str__(self):
        return self.holeName

class GolfTeam(models.Model):
    teamClub = models.ForeignKey('GolfClub', on_delete=models.CASCADE)
    teamName = models.CharField(max_length=200)
    teamEstablished = models.DateField(auto_now=False)
    isBanned = models.BooleanField(default=False)
    def __str__(self):
        return self.teamName

class GolfPlayer(models.Model):
    golfTeam = models.ForeignKey('GolfTeam',on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    dateOfBirth = models.DateField(auto_now=False)
    isBanned = models.BooleanField(default=False)
    HANDICAP_CHOICES = (
        (-18,"-18"),
        (-17,"-17"),
        (-16,"-16"),
        (-15,"-15"),
        (-14,"-14"),
        (-13,"-13"),
        (-12,"-12"),
        (-11,"-11"),
        (-10,"-10"),
        (-9,"-9"),
        (-8,"-8"),
        (-7,"-7"),
        (-6,"-6"),
        (-5,"-5"),
        (-4,"-4"),
        (-3,"-3"),
        (-2,"-2"),
        (-1,"-1"),
        (0,"0"),
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10"),
        (11,"11"),
        (12,"12"),
        (13,"13"),
        (14,"14"),
        (15,"15"),
        (16,"16"),
        (17,"17"),
        (18,"18"),


    )
    handicap = models.IntegerField(choices=HANDICAP_CHOICES)


    def __str__(self):
        return self.firstName+" "+self.secondName+", "+self.golfTeam.teamName+", "+self.golfTeam.teamClub.clubName

class Tournament(models.Model):
    dateTimeStart = models.DateTimeField(auto_now=False)
    dateTimeFinish = models.DateTimeField(auto_now=False)
    tournamentNotes = models.TextField(max_length=800)

    def __str__(self):
        return str(self.pk)

class TeamTournament(models.Model):
    tournamentName = models.CharField(max_length=200)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    GolfTeams = models.ManyToManyField('GolfTeam')
    def __str__(self):
        return self.tournamentName+", "+self.GolfTeams+", "+str(self.tournament.dateTimeStart)+" : "+str(self.tournament.dateTimeFinish)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import GolfClub,GolfCourse,CourseHole,GolfPlayer,GolfTeam,Tournament,TeamTournament

admin.site.register(GolfClub)
admin.site.register(GolfCourse)
admin.site.register(CourseHole)
admin.site.register(GolfPlayer)
admin.site.register(GolfTeam)
admin.site.register(Tournament)
admin.site.register(TeamTournament)

# Register your models here.

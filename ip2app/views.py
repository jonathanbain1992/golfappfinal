# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext

from django.http import HttpResponse
from django.views import View


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


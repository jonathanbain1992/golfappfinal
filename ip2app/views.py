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
    return HttpResponse("about page")

def SignInRegister(View):
    return HttpResponse("sign in or register ")

def Profile(View):
    return HttpResponse("profile")

def ScoreBoard(View):
    return HttpResponse("example scoreboard")

def Quiz(View):
    return HttpResponse("quiz page")

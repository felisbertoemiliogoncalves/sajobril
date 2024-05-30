import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import *
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect


from django.template.loader import render_to_string

from django.contrib.auth.models import Group




def index(request):
    context = {
        'pajinauma' : 'active',
    }
    return render(request,'visitor/uma.html', context)



def atividade(request):
    context = {
        'pajinaatividade' : 'active',
    }
    return render(request,'visitor/atividade.html', context)

def konaba(request):
    context = {
        'pajinakonaba' : 'active',
    }
    return render(request,'visitor/konaba.html', context)


def misa(request):
    context = {
        'pajinamisa' : 'active',
    }
    return render(request,'visitor/misa.html', context)


def eventu(request):
    context = {
        'pajinaeventu' : 'active',
    }
    return render(request,'visitor/eventu.html', context)


def anunsiu(request):
    context = {
        'pajinaanunsiu' : 'active',
    }
    return render(request,'visitor/anunsiu.html', context)


def atendimentu(request):
    context = {
        'pajinaatendimentu' : 'active',
    }
    return render(request,'visitor/atendimentu.html', context)


def planu(request):
    context = {
        'pajinaplanu' : 'active',
    }
    return render(request,'visitor/planu.html', context)


def detallu(request):
    context = {
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/detallu.html', context)

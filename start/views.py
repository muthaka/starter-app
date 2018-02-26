# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from decimal import Decimal
from django.contrib.auth import authenticate, login as auth_log
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.response import TemplateResponse
# from .models import starter
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import csv
from django.db.models import Sum
import json


def dashboard(request):
    return render_to_response('dashboard.html')

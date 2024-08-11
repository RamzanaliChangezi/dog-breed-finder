from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Push Notification
import json
from .models import *
# from .forms import *
from django.db.models import Q
from django.core.files.base import ContentFile




from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F
from wsgiref.util import FileWrapper
from django.http import FileResponse, HttpResponseNotFound, StreamingHttpResponse



# Constants
import os
from pathlib import Path
from django.db.models import Prefetch
from django.core.cache import cache
import random
from collections import defaultdict





def index(request):
    return render(request, 'index1.html')





def results(request):
    return render(request, "results.html")
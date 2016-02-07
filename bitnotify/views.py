from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse


def home_view(request):
    return render(request, 'home.html', {})



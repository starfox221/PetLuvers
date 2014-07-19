from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404, \
    HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render_to_response('home.html', locals(),context_instance=RequestContext(request))

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.get_profile()
    title = profile.tagline
    return render_to_response('profile.html', locals(),context_instance=RequestContext(request))

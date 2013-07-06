# From django mains
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# For dajaxice
from misc.dajaxice.core import dajaxice_functions

# From models

# From python
import datetime

def test(request):
    now=datetime.datetime.now()
    html = " <center><h1>Home page<br/></h1>Its %s now</center> " % now
    return HttpResponse(html)
    
def home(request):
    if request.method ==  'POST':
        data=request.POST.copy()
        contact=ContactRequests.objects.create(name=data['name'],email=data['email'],message=data['message'])
        contact.save()
        return HttpResponse('<center>Your request has been submitted succesfully</center>')
    else:
        return render_to_response ('base.html', {}, context_instance=RequestContext(request))

def template(request):
    return render_to_response ('template.html', {}, context_instance=RequestContext(request))
    
def blur(request):
    return render_to_response ('blur.html', {}, context_instance=RequestContext(request))
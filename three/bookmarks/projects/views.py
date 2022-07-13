from django.shortcuts import render
from .models import Project
import datetime

def signout(request):
    profile = request.user # it depends 
    if request.is_ajax(): # Do it with ajax
        logout(request)
        profile.last_time_logout = datetime.datetime.now()
        profile.save()
        return redirect("signin")
    raise PermissionDenied
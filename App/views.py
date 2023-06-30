from django.shortcuts import render,redirect
from django.contrib import messages
from App.youtube import *
from django.http import HttpResponse
# Create your views here.
def myhome(request):
    if request.method == "GET":
        # messages.error(request,'Please enter the link first')
        return render(request,"youtube.html")
    
    elif request.method == "POST":
        myurl = request.POST['data']
        if myurl is None:
            return HttpResponse("please enter the link")
        try:
            response = Youtube_conveter(myurl)
            messages.success(request, 'Download succesfully...')
        except:
            messages.info(request,"Video is already downloaded please delete is from the system first")
        return redirect('myhome')

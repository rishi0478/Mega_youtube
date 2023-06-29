from django.shortcuts import render,redirect
from django.contrib import messages
from App.youtube import *
# Create your views here.
def myhome(request):
    if request.method == "GET":
        return render(request,"index.html")
    
    elif request.method == "POST":
        myurl = request.POST['data']
        try:
            response = Youtube_conveter(myurl)
            messages.success(request, 'Download succesfully...')
        except:
            messages.info(request,"Something Went Wrong!")
        return redirect('myhome')

from django.shortcuts import render,redirect
from django.http  import HttpResponse
def work(request):
    
    return render(request, 'kazi.html',locals())

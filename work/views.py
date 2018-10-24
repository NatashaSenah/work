from django.http  import HttpResponse
def jirani(request):
    neighbours = Neighbourhood.objects.all()
    business = Business.objects.all()
    return render(request,'jirani.html',locals())

from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Buyer,Seller
from .forms import SellerForm,BuyerForm
from django.contrib.auth.models import User
def work(request):
    return render(request, 'kazi.html',locals())
@login_required(login_url='/accounts/login/')
def buyer(request):
    current_user = request.user
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            # print('edrftgyhunjmik,lp.;')

            buyer = form.save(commit=False)
            buyer.save()
        return redirect('home')


    else:
        form = BuyerForm()
    return render(request, 'buyer.html', {"form": form})
@login_required(login_url='/accounts/login/')
def seller(request):
    current_user = request.user
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            

            seller = form.save(commit=False)
            seller.save()
        return redirect('home')


    else:
        form = SellerForm()
    return render(request, 'seller.html', {"form": form})

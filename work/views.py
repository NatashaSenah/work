from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Buyer,Seller,Product
from .forms import SellerForm,BuyerForm,ProductForm
from django.contrib.auth.models import User
def work(request):
    all=Seller.objects.all()
    return render(request, 'kazi.html',locals())
@login_required(login_url='/accounts/login/')
def buyer(request):
    current_user = request.user
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():


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
def product(request):
    current_user = request.user
    if request.method == 'POST':
        print('llllllllllllllllllllllll')
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
        return redirect('home')


    else:
        form = ProductForm()
    return render(request, 'cart.html', {"form": form})

# @login_required(login_url='/login/')
# def profile(request):

#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm()

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'users/profile.html', context)


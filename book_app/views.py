from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic.edit import CreateView, DeleteView
from book_app.forms import UserForm, SellForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
import decimal
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Sell, Cart, custom_user
from . import views

# Create your views here.

def home(request):
    return render(request,'home.html')

def sign_up(request):
    if request.method=='POST':
        form=UserForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            obj=form.save(commit=False)
            obj.userlink_id=user.id
            obj.save()
            login(request, user)
            return redirect("home")
    form = UserForm()
    return render(request, 'sign_up.html', {'form': form})


def loginpage(request):
    form = AuthenticationForm(request.POST)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return render(request,'home.html')
    return render(request,'login.html',{'form':form})

@login_required
def logoutpage(request):
    logout(request)
    return redirect("home")

@login_required
def sellformcreated(request):
    return render(request,'sellformcreated.html')

@login_required
def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            ans = form.save(commit = False)
            ans.owner = request.user
            ans.save()
            return redirect("all_sell_items")
    return render(request,'sellform.html',{'form': SellForm()})

@login_required
def borrow(request):
    curr_user=custom_user.objects.get(userlink=request.user)
    books=Sell.objects.filter(pin_code=curr_user.user_pin).exclude(owner=request.user)
    return render(request,'borrow.html',{'books':books})

@login_required
def all_sell_items(request):
    books=Sell.objects.filter(owner=request.user)
    cnt=Sell.objects.filter(owner=request.user).count()
    return render(request,'sellformcreated.html',{'books':books,'count':cnt})

@login_required
def book_detail(request, uuid):
    book=Sell.objects.filter(pk=uuid)
    original_price=Sell.objects.get(id=uuid).price
    discount_price=Sell.objects.get(id=uuid).discount
    if discount_price=="40%":
        x=40
    elif discount_price=="50%":
        x=50
    elif discount_price=="60%":
        x=60
    elif discount_price=="70%":
        x=70
    elif discount_price=="80%":
        x=80
    elif discount_price=="90%":
        x=90
    else:
        x=100
    x=decimal.Decimal(x)*decimal.Decimal(original_price)*decimal.Decimal(0.01)
    x=round(x,2)
    x=decimal.Decimal(original_price)-x
    return render(request,'book_detail.html',{'books':book,'original':original_price,'selling':x})

@login_required
def all_cart_items(request):
    cart_items=Cart.objects.all()
    cnt=Cart.objects.all().count()
    print(cart_items)
    return render(request,"all_cart_items.html",{'cart_items':cart_items,'count':cnt})

@login_required
def add_to_cart(request,uuid):
    cnt=Cart.objects.filter(seller_id=uuid).count()
    if cnt:
        pass
    else:
        cart_item=get_object_or_404(Sell, pk=uuid)
        obj=Cart(seller=cart_item)
        obj.save()
    cart_items=Cart.objects.all()
    cnt=Cart.objects.all().count()
    return render(request,"add_to_cart.html",{'cart_items':cart_items,'count':cnt})


class delete_from_cart(DeleteView):
    model=Cart
    success_url=reverse_lazy("all_cart_items")

@login_required
def search(request):
    input_q=request.GET.get("search_title")
    searched_items=Sell.objects.filter(book_name__icontains=input_q)
    return render(request,'borrow.html',{'books':searched_items}) 

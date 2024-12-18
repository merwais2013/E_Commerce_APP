from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.db.models import Q
import json


from .models import Product, Category, Profile
from .forms import SignupForm, UserUpdateForm, UserUpdatePasswordForm, UpdateUserInfoForm
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress

def home(request):
  products = Product.objects.all()
  return render(request, template_name="index.html", context={"products": products})

def about(request):
  return render(request, template_name="about.html")


def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '').strip()
        if not searched:  # Check if input is empty
            messages.warning(request, "Please enter a product name to search.")
            return render(request, template_name="search.html")

        # Perform the search
        searched_products = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        if not searched_products:
            messages.info(request, "The Product is not currently available!")

        return render(
            request,
            template_name="search.html",
            context={"searched": searched_products}
        )
    return render(request, template_name="search.html")



def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      current_user = Profile.objects.get(user__id=request.user.id)
      saved_cart = current_user.old_cart
      if saved_cart:
        converted_cart = json.loads(saved_cart)
        cart = Cart(request)
        for key, value in converted_cart.items():
          cart.db_add(product=key, quantity=value)
      messages.success(request, "You have successfully logged In!")
      return redirect('home')
    else:
      messages.success(request, "Please check your username or password!")
      return redirect('login-user')
  return render(request, template_name="login_user.html")

def logout_user(request):
  logout(request)
  messages.success(request, "You have successfully logged out!")
  return redirect('login-user')

def signup_user(request):
  form = SignupForm()
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid:
      form.save()
      username = form.cleaned_data['username']
      password1 = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password1)
      login(request, user)
      messages.success(request, "You have successfully created your account!🤗")
      return redirect('update-info')
    else:
      messages.success(request, "A problem has happend to your registeration. try again!😥")
      return redirect('signup-user')
  else:
    return render(request, template_name="sign_up.html", context={"form": form})


def update_user(request):
  if request.user.is_authenticated:
    current_user = User.objects.get(id=request.user.id)
    user_form = UserUpdateForm(request.POST or None, instance=current_user)
    if user_form.is_valid():
      user_form.save()
      login(request, current_user)
      messages.success(request, "Your profile updated successfully")
      return redirect('home')
    else:
      return render(request, template_name="update_user.html", context={"form": user_form})
  else:
    messages.warning(request, "Please login first!")
    return redirect('home')

def update_info(request):
  if request.user.is_authenticated:
    current_user = Profile.objects.get(user__id=request.user.id)
    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
    form = UpdateUserInfoForm(request.POST or None, instance=current_user)
    shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    if form.is_valid() or shipping_form.is_valid():
      form.save()
      shipping_form.save()
      messages.success(request, "Your Info updated successfully")
      return redirect('home')
    return render(request, template_name="update_info.html", context={"form":form, "shipping_form": shipping_form})
  else:
    messages.warning(request, "Please login first!")
    return redirect('home')


def update_password(request):
  if request.user.is_authenticated:
    current_user = request.user
    if request.method == "POST":
      form = UserUpdatePasswordForm(current_user, request.POST)
      if form.is_valid():
        form.save()
        messages.success(request, "Your password has successfully changed!🎉")
        login(request, current_user)
        return redirect('update-user')
      else:
        for error in list(form.errors.values()):
          messages.error(request, error)
          return redirect('update-password')
    else:
      form = UserUpdatePasswordForm(current_user)
      return render(request, template_name="update_password.html", context={"form": form})
  else:
    messages.warning(request, "Please login first!☺")



def product(request, pk):
  product = Product.objects.get(id=pk)
  return render(request, template_name="product.html", context={"product": product})

def category(request, cat):
  cat = cat.replace("-", " ")
  try:
    category = Category.objects.get(name=cat)
    products = Product.objects.filter(category=category)
    return render(request, template_name="category.html", context={"products": products, "category": category})
  except:
    messages.success(request, "This type of category is not available.😥")
    return redirect("home")


def category_summary(request):
  all_cat = Category.objects.all()
  return render(request, "category_summary.html", {"category": all_cat})
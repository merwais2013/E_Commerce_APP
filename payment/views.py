from django.shortcuts import render
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress

def payment(request):
  return render(request, template_name="payment.html")

def checkout(request):
  cart = Cart(request)
  cart_products = cart.get_prods()
  quantities = cart.get_quants()
  total = cart.get_total()
  if request.user.is_authenticated:
    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
    shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    return render(request, template_name="checkout.html", context={"cart_products": cart_products, "quantities": quantities, "total": total, "shipping_form":shipping_form})
  else:
    shipping_form = ShippingForm(request.POST or None)
    return render(request, template_name="checkout.html", context={"cart_products": cart_products, "quantities": quantities, "total": total, "shipping_form":shipping_form})

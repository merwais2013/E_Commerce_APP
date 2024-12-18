from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .cart import Cart
from shop.models import Product


def cart_summary(request):
  cart = Cart(request)
  cart_products = cart.get_prods()
  quantities = cart.get_quants()
  total = cart.get_total()
  return render(request, template_name="cart_summary.html", context={"cart_products": cart_products, "quantities": quantities, "total": total})

def cart_add(request):
  cart = Cart(request)
  if request.POST.get('action') == 'post':
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    product =  get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=product_qty)

    # response = JsonResponse({"Product Name": product.name})
    cart_quantity = cart.__len__()
    response = JsonResponse({'qty': cart_quantity})
    messages.success(request, "You have successfully added the product to your cart!🤗")
    return response

from django.http import JsonResponse

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            cart.update(product=product_id, quantity=product_qty)
            messages.success(request, "You have successfully updated your cart!🤗")
            return JsonResponse({'qty': product_qty})  # Ensure 'qty' is in the response
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input'}, status=400)
    return JsonResponse({'error': 'Invalid action'}, status=400)

def cart_delete(request):
  cart = Cart(request)
  if request.POST.get('action') == 'post':
    try:
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        messages.success(request, "You have successfully removed the product from your cart!🤗")
        return JsonResponse({'product': product_id})  # Ensure 'qty' is in the response
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid input'}, status=400)
  return JsonResponse({'error': 'Invalid action'}, status=400)


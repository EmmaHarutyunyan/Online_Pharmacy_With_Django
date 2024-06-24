from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.db.models import Sum
from .models import Slide, Home_products, Product, About, ContactUs, CartItem



def index(request):
    slides = Slide.objects.all()
    home_products = Home_products.objects.all()
    return render(request, 'main/index.html', {
        'slides': slides,
        'home_products': home_products
    })


def about(request):
    about = About.objects.first()
    return render(request, 'main/about.html', {
        'about': about
    })


def cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('update_quantity'):
                cart_item_id, action = value.split('-')
                cart_item = CartItem.objects.get(pk=cart_item_id)
                if action == 'minus':
                    if cart_item.quantity > 1:
                        cart_item.quantity -= 1
                elif action == 'plus':
                    cart_item.quantity += 1
                cart_item.save()
        return redirect('cart')

    cart_items = CartItem.objects.all()
    subtotal = sum(
        item.quantity * (
            item.product.sale_price if item.product.on_sale and item.product.sale_price < item.product.price else item.product.price
        )
        for item in cart_items
    )
    total_sum = subtotal  

    return render(request, 'main/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_sum': total_sum,
    })



def cart_add(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')
    return redirect('shop')


def cart_remove(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('cart')


def checkout(request):
    return render(request, 'main/checkout.html')


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('c_fname')
        lname = request.POST.get('c_lname')
        email = request.POST.get('c_email')
        message = request.POST.get('c_message')
        ContactUs.objects.create(fname=fname, lname=lname, email=email, message=message)
        return HttpResponseRedirect('/thankyou/')
    return render(request, 'main/contact.html')


def main(request):
    return render(request, 'main/main.html')


def shop_single(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        product = None
    context = {
        'product': product,
    }
    return render(request, 'main/shop_single.html', context)


def shop(request):
    filter_price1 = request.GET.get('min_price', '')
    filter_price2 = request.GET.get('max_price', '')

    if filter_price1 == '':
        filter_price1 = 0
    if filter_price2 == '':
        max_price_obj = Product.objects.aggregate(Max('price'))
        filter_price2 = max_price_obj['price__max'] if max_price_obj['price__max'] else 0

    products = Product.objects.filter(price__range=(filter_price1, filter_price2))

    sort = request.GET.get('sort', '')
    if sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    context = {
        'products': products
    }
    return render(request, 'main/shop.html', context)


def thankyou(request):
    return render(request, 'main/thankyou.html')

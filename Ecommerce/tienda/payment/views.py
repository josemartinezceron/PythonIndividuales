from django.shortcuts import render

from . models import ShippingAddress, Order, OrderItem
from cart.cart import Cart

from django.http import JsonResponse

# Create your views here.
def checkout(request):
    #usuarios con cuenta
    if request.user.is_authenticated:
        try:
            #usuario autenticado con datos de despacho
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context: {'shipping':shipping_address}
            return render(request,'payment/checkout.html', context=context)
        except:
            #usuarios con informacion sin datos
             return render(request,'payment/checkout.html')
    
    else :
        # usuarios no registrados
        return render(request,'payment/checkout.html')
    return render(request, 'payment/checkout.html')

def payment_success(request):
    #limpiar carro
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')

def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        # direccion de envio completa
        shipping_address = (address1 + "\n" + address2 + "\n" + city + "\n" + state )
        # Informacion del carro
        cart = Cart(request)
        #costo total de todos los items
        total_cost = cart.get_total()
        #1) Crear Orden -> Cuentas de Usuario con o sin Informacion de despacho
        if request.user.is_authenticated:
            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost, user=request.user)
            order_id = order.pk
            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'], user=request.user)
        #2) Crear Orden -> Usuarios sin cuenta
        else:
            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost,)
            order_id = order.pk
            for item in cart:
                    OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'])

        order_success = True
        response = JsonResponse({'success':order_success})
        return response
                

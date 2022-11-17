from django.shortcuts import render
from django.contrib import messages

from .models import Order
from .forms import OrderForm

def checkoutView(request):
    """
        This view loads the checkout page
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Oops, looks like there is nothing in your basket yet.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    comtext = {
        'order_form': order_form,
    }

    return render(request, template, context)
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def PaymentMain(request):
    # return render(request, '<html><body>This is main.</body></html>', {})
    return render(request, 'Bokwang.templeates.payment')


def Index(request):
    return HttpResponse("Hello, world. You're at the **Payment** index.")
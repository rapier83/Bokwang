from django.http import HttpResponse
from django.shortcuts import render


def PayMain(request):
    # request must be given, even it doesn't use
    return render(request, 'Payment/base.html', {})
    # return HttpResponse('<html><body>This is pay. main.</body></html>')


def Base(request):
    return HttpResponse("Hello, world. You're at the **Payment** index.")

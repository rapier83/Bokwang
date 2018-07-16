from django.http import HttpResponse


def PaymentMain(request):
    # return render(request, '<html><body>This is main.</body></html>', {})
    return HttpResponse('<html><body>This is pay. main.</body></html>')


def Index(request):
    return HttpResponse("Hello, world. You're at the **Payment** index.")
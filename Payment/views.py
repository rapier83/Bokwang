from django.http import HttpResponse


def paymentMain(request):
    # return render(request, '<html><body>This is main.</body></html>', {})
    return HttpResponse('<html><body>This is pay. main.</body></html>')

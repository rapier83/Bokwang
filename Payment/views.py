from django.shortcuts import render



def index(request):
    return render(request, '<html><body>This is index.</body></html>', {})


def paymentMain(request):
    return render(request, 'payment/main.html', {})

def detail(request):
    return render(request, '<html><body>404 Error. Page Not Found.</body></html>', {})

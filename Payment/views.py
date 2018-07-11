from django.shortcuts import render
from django.http import HttpResponse


def index():
    # return render(request, '<html><body>This is index.</body></html>', {})
    return HttpResponse('<html><body>This is index.</body></html>')


def paymentMain():
    # return render(request, '<html><body>This is main.</body></html>', {})
    return HttpResponse('<html><body>This is pay. main.</body></html>')


def detail():
    # return render(request, '<html><body>404 Error. Page Not Found.</body></html>', {})
    return HttpResponse('<html><body>This is pay. 404.</body></html>')

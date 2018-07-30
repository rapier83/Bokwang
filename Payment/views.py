from django.http import HttpResponse
from django.shortcuts import render

P = []

def PayMain(request: object) -> object:
    # request must be given, even it doesn't use
    return render(request, 'base.html', {'PaperList': None})
    # return HttpResponse('<html><body>This is pay. main.</body></html>')


def Base(request):
    return HttpResponse("Hello, world. You're at the **Payment** index.")


def YearArchive(request, year):
    ListByYear = 0000
    return HttpResponse("<h2> years </h2>")


def ViewPapar(request):
    return HttpResponse("<h2> the paper </h2>")

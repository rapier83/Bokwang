from django.urls import path
from . import views

urlpatterns = [
    path('', views.PayMain, name='index'),
    path('<int:year>', views.YearArchive, name='Year Archive'),
    path('<int:year>/<int:month>', views.ViewPapar)
]
from django.urls import include, path


urlpatterns = [
    path(r'', include('Payment.urls')),
]
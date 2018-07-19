from django import forms
from .models import Order

class PostForm(forms.ModelForm):

    class Meta:
        model = Order.Paper
        fields = ('Delivered Date', 'OrderedCompany', 'SaveLocation')


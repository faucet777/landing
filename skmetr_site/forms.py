from django.forms import ModelForm
from django import forms

from skmetr_site.models import Tickets


class FeedbackForm(forms.ModelForm):
    client_email = forms.EmailField(label='Электронная Почта')
    client_phone = forms.IntegerField(label='Телефон')
    client_name = forms.CharField(label='Ваше Имя')
    ticket_subject = forms.CharField(label='Ваше Обращение', widget=forms.Textarea(attrs={'class': 'form-input','rows':5, 'cols':60}))
    class Meta:
        model = Tickets
        fields = ('client_email', 'client_phone', 'client_name', 'ticket_subject')
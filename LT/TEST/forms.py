from django import forms

from .models import Locomotive, Branch, Period


class LTForm(forms.Form):
    filial = forms.ModelChoiceField(queryset=Branch.objects.all())
    locomotive = forms.ModelChoiceField(queryset=Locomotive.objects.all())
    period = forms.ModelChoiceField(queryset=Period.objects.all())


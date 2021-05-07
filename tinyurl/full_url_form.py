from django import forms


class FullUrlForm(forms.Form):
    url = forms.CharField(label='Enter your URL')
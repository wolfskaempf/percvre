from django import forms


class TokenForm(forms.Form):
    token = forms.CharField(label="Token", min_length=1, max_length=64)

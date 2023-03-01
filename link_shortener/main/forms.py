from django import forms


class LinkForm(forms.Form):
    """Форм генерации ссылки"""
    link = forms.CharField()

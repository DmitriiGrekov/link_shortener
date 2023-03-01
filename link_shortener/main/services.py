from django.shortcuts import render
from .forms import LinkForm
from .models import Link


def validation_link_form(request):
    """Валидация формы"""
    form = LinkForm(request.POST)
    if form.is_valid():
        link = save_link(form)
        return render(request, 'main/index.html', {'code': link.code})
    return render(request, 'main/index.html')


def save_link(form):
    """Сохранение ссылки"""
    user_link = form.cleaned_data['link']
    link = Link.objects.create(original_link=user_link)
    return link

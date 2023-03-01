from django.shortcuts import render
from .models import Link
from django.shortcuts import redirect
from .services import validation_link_form


def main_page(request):
    """Вывод формы и создание сокращенной ссылки"""
    if request.method == 'POST':
        return validation_link_form(request)
    else:
        return render(request, 'main/index.html')


def redirect_user(request, code):
    """Перенаправление пользователя"""
    link = Link.objects.get(code=code)
    return redirect(link.original_link)

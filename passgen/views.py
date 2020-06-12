import random
import string

from django.shortcuts import render


def home(request):
    return render(request, 'passgen/home.html')


def password(request):
    size = int(request.GET.get('length', 18))
    symbols = '!@#$%^&*()'
    chars = string.ascii_lowercase
    if request.GET.get('uppercase'):
        chars = chars + string.ascii_uppercase
    if request.GET.get('numbers'):
        chars = chars + string.digits
    if request.GET.get('special'):
        chars = chars + symbols
    return render(request, 'passgen/home.html', {'password': ''.join(random.choice(chars) for _ in range(size))})

import random
import string

from django.shortcuts import render
from django.http import JsonResponse

symbols = '!@#$%^&*()'


def generate_password(
    length=18,
    is_uppercase=False,
    has_numbers=False,
    has_special_chars=False,
):
    chars = string.ascii_lowercase
    if is_uppercase:
        chars = chars + string.ascii_uppercase

    if has_numbers:
        chars = chars + string.digits

    if has_special_chars:
        chars = chars + symbols

    # just copy-pasted
    return ''.join(random.choice(chars) for _ in range(length))


def home(request):
    return render(request, 'passgen/home.html', {password: generate_password()})


def password(request):
    return JsonResponse({
        'password': generate_password(
            # prone to errors (use 'try' here and double-check),
            length=int(request.GET.get('length', 18)),

            is_uppercase='uppercase' in request.GET,
            has_numbers='numbers' in request.GET,
            has_special_chars='special' in request.GET,
        )
    })



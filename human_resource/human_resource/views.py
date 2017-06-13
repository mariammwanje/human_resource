from django.shortcuts import render


# from django.contrib.auth.decorators import login_required
# @login_required(login_url='accounts:login')


def home(request):
    return render(request, '../templates/landing.html')


def admin_menu(request):
    return render(request, '../templates/admin_menu.html')
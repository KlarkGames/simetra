from django.shortcuts import render
from .models import Boss, Employee


def main_page(request):
    context = {'bosses_list': Boss.objects.all(),
               'employees_list': Employee.objects.all()}
    return render(request, 'simetra_app/main.html', context)


def methodology_page(request):
    return render(request, 'simetra_app/methodology.html')
from django.shortcuts import render
import random
# Import models to view
from .models import Visitor

# Create your views here.

def header(request):
    return render(request, 'main/header.html')
def home(request):
    visitors = Visitor.objects.all()
    return render(request, 'subpages/index.html', {'visitors':visitors})
def generatedPassword(request):
    passwordResult = ''
    # Default is 12 characters in case user didn't choose
    length = int(request.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper_case'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWZYX')
    if request.GET.get('number_case'):
        characters.extend('123456789')
    if request.GET.get('special_char'):
        characters.extend('@#$%')
    for x in range(length):
        passwordResult += random.choice(characters)

    return render(request, 'subpages/pass.html', {'password': passwordResult})
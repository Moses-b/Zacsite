from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def main_view(request):
    return render(request, 'views/main.htm', {'name': 'ZAcademy'})

#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
@login_required
def home_view(request):
    return render(request, 'views/home.htm')
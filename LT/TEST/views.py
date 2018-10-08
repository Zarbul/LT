from django.http import QueryDict
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from .models import Branch
from .models import Locomotive
from .models import Period
from .forms import LTForm



def home(request):
    list_branch = Branch.objects.all
    list_locomotive = Locomotive.objects.all
    list_period = Period.objects.all
    form = LTForm(request.GET)
    if request.GET:
        filial = request.GET['filial']
        locomotive = request.GET['locomotive']
        period = int(request.GET['period'])
        print(filial, locomotive, period, 'periodssss', type(period))
        # if filial in list_branch:
        #     print('ok')
    else:
        filial = 0
        locomotive = 0
        year = [i for i in range(2017, 2022)]
        period = ""
        for i in year:
            period = period + str(i) + "," + " "

    content = {
        'branches': list_branch,
        'locomotives': list_locomotive,
        'periods': list_period,
        'chart_period': period,
        'form': form,
        'username': auth.get_user(request).username,
    }
    return render(request, 'home.html', content)




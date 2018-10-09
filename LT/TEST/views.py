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
        filial = int(request.GET['filial'])
        locomotive = int(request.GET['locomotive'])
        year = int(request.GET['period'])
        print(filial, locomotive, year, 'periodssss', type(year))
        # if filial in list_branch:
        #     print('ok')
    else:
        filial = 0
        locomotive = 0
        years = [i for i in range(2017, 2022)]
        year = ""
        for i in years:
            year = year + str(i) + "," + " "
        print(year, filial, locomotive,  'periodssss', type(year))

    content = {
        'branches': list_branch,
        'locomotives': list_locomotive,
        'train': locomotive,
        'filial': filial,
        'periods': list_period,
        'chart_period': year,
        'form': form,
        'username': auth.get_user(request).username,
    }
    return render(request, 'home.html', content)




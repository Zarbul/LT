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
    obj = {}
    arr = []
    if request.GET:
        filial = int(request.GET['filial'])
        train = int(request.GET['locomotive'])
        year = int(request.GET['period'])
        print(filial, train, year, 'periodssss', type(year))



    else:
        filial = 0
        train = 0
        # years = [i for i in range(2017, 2022)]
        year = 0
        # for i in years:
        #     year = year + str(i) + "," + " "
        print(year, filial, train, 'periodssss', type(year))

    content = {
        'branches': list_branch,
        'locomotives': list_locomotive,
        'train': train,
        'filial': filial,
        'periods': list_period,
        'chart_period': year,
        'form': form,
        'username': auth.get_user(request).username,
    }
    return render(request, 'home.html', content)


def index(request):
    list_branch = Branch.objects.all()
    list_locomotive = Locomotive.objects.all()
    list_period = Period.objects.all()

    data = 0
    labels = 0
    obj = {}

    if request.GET:
        filial = int(request.GET['filial'])
        train = int(request.GET['locomotive'])
        year = int(request.GET['period'])

        if train > 0:
            for i in list_locomotive:
                for j in list_period:
                    if i.id == train:
                        # all data
                        if j.year == year and j.locomotive_id == i.id and j.branch_id == filial:
                            data = i.rate * j.run
                            labels = year
                        # one train one year all filials
                        elif j.year == year and filial == 0 and j.locomotive_id == i.id:
                            data += i.rate * j.run
                            labels = year
                        # all year one train one filial
                        elif j.branch_id == filial and year == 0 and j.locomotive_id == i.id:
                            if j.year in obj:
                                obj[j.year] += i.rate * j.run
                            else:
                                obj[j.year] = i.rate * j.run
                        # all years all filials one train
                        elif filial == 0 and year == 0 and j.locomotive_id == i.id:
                            if j.year in obj:
                                obj[j.year] += i.rate * j.run
                            else:
                                obj[j.year] = i.rate * j.run
        elif train == 0:
            # one filial one year all train
            if filial > 0 and year > 0:
                for j in list_period:
                    for i in list_locomotive:
                        if j.locomotive_id == i.id:
                            data += i.rate * j.run
                            labels = year
            # all years
            elif filial == 0 and year == 0:
                for j in list_period:
                    for i in list_locomotive:
                        if j.locomotive_id == i.id:
                            if j.year in obj:
                                obj[j.year] += i.rate * j.run
                            else:
                                obj[j.year] = i.rate * j.run

            # only one year
            elif filial == 0 and year > 0:
                for j in list_period:
                    if j.year == year:
                        for i in list_locomotive:
                            if j.locomotive_id == i.id:
                                data += i.rate * j.run
                                labels = year
            # one filial all year all train
            elif filial > 0 and year == 0:
                for j in list_period:
                    if j.branch_id == filial:
                        for i in list_locomotive:
                            if j.locomotive_id == i.id:
                                if j.year in obj:
                                    obj[j.year] += i.rate * j.run
                                else:
                                    obj[j.year] = i.rate * j.run

    content = {
        # for form
        'branches': list_branch,
        'locomotives': list_locomotive,
        'periods': list_period,
        # for data in chart
        'data': data,
        'labels': labels,
        'obj': obj,

        'username': auth.get_user(request).username,
    }
    return render(request, 'index.html', content)

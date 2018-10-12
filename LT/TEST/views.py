from django.http import QueryDict, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from .models import Branch
from .models import Locomotive
from .models import Period
from .forms import LTForm


def chart(request):
    filial = int(request.GET.get('filial', 0))
    locomotive = int(request.GET.get('locomotive', 0))
    period = int(request.GET.get('period', 0))

    list_locomotive = Locomotive.objects.all()
    list_period = Period.objects.all()

    obj = {}

    if locomotive > 0:
        for i in list_locomotive:
            for j in list_period:
                if i.id == locomotive:
                    # all data
                    if j.year == period and j.locomotive_id == i.id and j.branch_id == filial:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run
                    # one train one year all filials
                    elif j.year == period and filial == 0 and j.locomotive_id == i.id:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run
                    # all year one train one filial
                    elif j.branch_id == filial and period == 0 and j.locomotive_id == i.id:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run
                    # all years all filials one train
                    elif filial == 0 and period == 0 and j.locomotive_id == i.id:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run
    elif locomotive == 0:
        # one filial one year all train
        if filial > 0 and period > 0:
            for j in list_period:
                for i in list_locomotive:
                    if j.locomotive_id == i.id:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run
        # all years
        elif filial == 0 and period == 0:
            for j in list_period:
                for i in list_locomotive:
                    if j.locomotive_id == i.id:
                        if j.year in obj:
                            obj[j.year] += i.rate * j.run
                        else:
                            obj[j.year] = i.rate * j.run

        # only one year
        elif filial == 0 and period > 0:
            for j in list_period:
                if j.year == period:
                    for i in list_locomotive:
                        if j.locomotive_id == i.id:
                            if j.year in obj:
                                obj[j.year] += i.rate * j.run
                            else:
                                obj[j.year] = i.rate * j.run
        # one filial all year all train
        elif filial > 0 and period == 0:
            for j in list_period:
                if j.branch_id == filial:
                    for i in list_locomotive:
                        if j.locomotive_id == i.id:
                            if j.year in obj:
                                obj[j.year] += i.rate * j.run
                            else:
                                obj[j.year] = i.rate * j.run

    return JsonResponse(obj)


def index(request):
    list_branch = Branch.objects.all()
    list_locomotive = Locomotive.objects.all()
    list_period = Period.objects.all()


    content = {
        # for form
        'branches': list_branch,
        'locomotives': list_locomotive,
        'periods': list_period,

        'username': auth.get_user(request).username,
    }
    return render(request, 'index.html', content)

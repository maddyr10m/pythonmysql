from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BurnRate, BurnDetail
from .forms import RegistrationForm, DetailForm

# Create your views here.


def home(request):

    return render(request, 'home.html')


def UpdateExp(request):
    context = {"form": RegistrationForm,
               "formD": DetailForm}
    return render(request, 'UpdateExp.html', context)


def reports(request):
    obj = BurnRate.objects.get(id=1)
    context = {"data": obj}
    return render(request, 'reports.html', context)


def addData(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
      myregister = BurnRate(myitem=form.cleaned_data['myitem'],
                            paymethod=form.cleaned_data['paymethod'],
                            cost=form.cleaned_data['cost'],
                            pub_date=form.cleaned_data['pub_date'])
    myregister.save()
    return redirect('UpdateExp')


def addDetailData(request):
    formD = DetailForm(request.POST)

    if formD.is_valid():
      dregister = BurnDetail(fkey=formD.cleaned_data['fkey'],
                            myitem=formD.cleaned_data['myitem'],
                            count_item=formD.cleaned_data['count_item'],
                            itemclass=formD.cleaned_data['itemclass'],
                            spendgroup=formD.cleaned_data['spendgroup'],
                            gengroup=formD.cleaned_data['gengroup'],
                            cost=formD.cleaned_data['cost'],
                            taxrate=formD.cleaned_data['taxrate'],
                            costwithtax=formD.cleaned_data['costwithtax'])
    dregister.save()
    return redirect('home')
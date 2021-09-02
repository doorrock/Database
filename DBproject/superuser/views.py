from django.shortcuts import render, redirect

# Create your views here.
from superuser.models import Affilate, Company


def adminCode(request):
    if request.method == "GET":
        print("okay now")
        return render(request, 'admincode.html')
    elif request.method == "POST":
        code = request.POST.get('admincode',None)
        print(code)
        if code == "0000":
            print("you are super")
            return render(request, 'option.html')
        else:
            print("??? who are you")
            return render(request, 'admincode.html')

def hire_info(request):
    affilates = Affilate.objects.all()
    info = {'affilates':affilates}
    if request.method == "GET":
        return render(request, 'hire_info.html', info)
    elif request.method == "POST":
        c_aff = request.POST.get('c_aff', None)
        c_name = request.POST.get('c_name', None)
        c_type = request.POST.get('c_type', None)
        c_start_date = request.POST.get('c_start_date', None)
        c_end_date = request.POST.get('c_end_date', None)

        company_a = Affilate(affilate=c_aff, c_name=Company.objects.get(name=c_name), type=c_type, start_date=c_start_date, end_date=c_end_date)
        company_a.save()

        return render(request, 'hire_info.html', info)
    else:
        return render(request, 'hire_info.html', info)

def company_info(request):
    companies = Company.objects.all()
    info = {'companies':companies}
    if request.method == "GET":
        return render(request, 'company_info.html', info)
    elif request.method == "POST":
        name = request.POST.get('name', None)
        owner = request.POST.get('owner', None)
        date = request.POST.get('date', None)
        marketC = request.POST.get('marketC', None)
        intro = request.POST.get('intro', None)

        company_i = Company(name=name, owner=owner, date=date, marketC=marketC, intro=intro)
        company_i.save()

        return render(request, 'company_info.html', info)
    else:
        return render(request, 'company_info.html', info)
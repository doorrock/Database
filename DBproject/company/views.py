from django.shortcuts import render, redirect, HttpResponse
from superuser.models import Affilate, Company
from company.models import MyCompany, Review
from user.models import User
# Create your views here.
def list(request):
    affilates = Affilate.objects.all()
    info = {'affilates': affilates}
    if request.method == "GET":
        return render(request, 'list.html', info)
    elif request.method == "POST":
        userid = request.session['user_id']
        affilate = request.POST.get('affilate', None)
        c_name = request.POST.get('c_name', None)
        type = request.POST.get('type', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)

        my_company = MyCompany(user_id=User.objects.get(user_id=userid), aff_name=Affilate.objects.get(affilate=affilate),
                               c_name=c_name, type=type, start_date=start_date, end_date=end_date)
        my_company.save()
        return render(request, 'list.html', info)
    elif request.method == "POST2":
        c_aff = request.POST.get('c_aff', None)
        return HttpResponse('2')

def info(request):
    companies = Company.objects.all()
    info = {'companies': companies}
    if request.method == "GET":
        return render(request, 'info.html', info)

def review(request):
    reviews = Review.objects.all()
    info = {'reviews': reviews}
    if request.method == "GET":
        return render(request, 'review.html', info)
    elif request.method == "POST":
        userid = request.session['user_id']
        affilate = request.POST.get('affilate', None)
        review = request.POST.get('review', None)

        re = Review(user_id=User.objects.get(user_id=userid), aff_name=Affilate.objects.get(affilate=affilate),
                               review=review)
        re.save()
        return render(request, 'review.html', info)

def mypage(request, userid):
    # userid = request.session['user_id']
    items = MyCompany.objects.filter(user_id=userid).values()
    info = {'items': items}
    return render(request, 'mypage.html', info)

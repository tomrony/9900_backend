from django.shortcuts import render

# Create your views here.
from .models import GISAID

# def user_list(request):
#     users = User.objects.all()
#     for i in users:
#         print(i.username, i.password)
#     return render(request,'user_list.html', {"users":users})


def data_list(request):
    data = GISAID.objects.all()
    for i in data:
        print(i.variant,i.city,i.province,i.date)

    return render(request, 'data_list.html', {"data": data})


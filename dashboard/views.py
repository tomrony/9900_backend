from django.shortcuts import render

# Create your views here.
from .models import GISAID




def data_list(request):
    data = GISAID.objects.all()
    for i in data:
        print(i.variant,i.city,i.province,i.date)

    return render(request, 'data_list.html', {"data": data})

def filter(request):
    data = GISAID.objects.filter()


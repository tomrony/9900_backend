from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import GISAID, Division, Location, Pangolin

# @csrf_exempt
def covid_data(request):
    if request.method == 'GET':
        year = request.GET.get('year', '2023')
        data = []
        for province in Division.objects.all():
            total_cases = GISAID.objects.filter(division=province, date__year=year).count()
            data.append({
                'province': province.division,
                'total_cases': total_cases,
            })

        return JsonResponse(data, safe=False)
from django.db.models import Count
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import GISAID, Division
from django.http import JsonResponse



# def data_list(request):
#     data = GISAID.objects.all()
#     for i in data:
#         print(i.variant,i.city,i.province,i.date)
#
#     return render(request, 'data_list.html', {"data": data})
#
# def filter(request):
#     data = GISAID.objects.filter()

# @csrf_exempt
def covid_data(request):
    if request.method == 'GET':
        year = request.GET.get('year', '2021')
        province_name = request.GET.get('province', 'Anhui')
        month = request.GET.get('month', 'January')

        try:
            province = Division.objects.get(division=province_name)
        except Division.DoesNotExist:
            return JsonResponse({'error': 'Province not found'}, status=404)

        # Initially filters by the division and year
        filters = {
            'division': province,
            'date__year': year
        }

        # If a month is provided, add the month to the filters.
        if month:
            filters['date__month'] = month

        gisaid_records = GISAID.objects.filter(**filters).values('date').annotate(total_cases=Count('id'))

        cases_by_date = {
            record['date'].strftime('%Y-%m-%d'): {'total': record['total_cases'],
                'new': record['total_cases']} for record in gisaid_records
        }

        response_data = {
            'cases': cases_by_date,
            'year': year,
            'province': province_name,
        }

        return JsonResponse(response_data)
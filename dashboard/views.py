from django.db.models import Count
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from .models import GISAID, Division
from django.http import JsonResponse

# @csrf_exempt
def charts_data(request):
    if request.method == 'GET':
        year = request.GET.get('year', '2021')
        province_name = request.GET.get('province', 'Anhui')
        month_name = request.GET.get('month', 'January')

        month_mapping = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
        }

        month = month_mapping.get(month_name, 1)  # Default to January if month not found

        try:
            province = Division.objects.get(division=province_name)
        except Division.DoesNotExist:
            return JsonResponse({'error': 'Province not found'}, status=404)

        # Initially filters by the division and year
        filters = {
            'division': province,
            'date__year': year,
            'date__month': month
        }

        gisaid_records = GISAID.objects.filter(**filters).values('date').annotate(new_cases=Count('id'))


        cases_by_date = {
            record['date'].strftime('%Y-%m-%d'): {
                'new': record['new_cases']
            } for record in gisaid_records
        }

        total_new_cases = sum(record['total_cases'] for record in gisaid_records)


        response_data = {
            'cases': dict(sorted(cases_by_date.items())),
            'year': year,
            'province': province_name,
            'total': total_new_cases
        }

        print(response_data)  # Log the response data to check it
        return JsonResponse(response_data)

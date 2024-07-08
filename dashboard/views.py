from django.db.models import Count
# from django.views.decorators.csrf import csrf_exempt
from .models import GISAID, Division
from django.http import JsonResponse

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


def new_cases(filters):
    gisaid_records = GISAID.objects.filter(**filters).values('date').annotate(new_cases=Count('id'))
    cases_by_date = {
        record['date'].strftime('%Y-%m-%d'): {
            'new': record['new_cases']
        } for record in gisaid_records
    }
    total_new_cases = sum(record['new_cases'] for record in gisaid_records)
    return dict(sorted(cases_by_date.items())), total_new_cases


# @csrf_exempt
def charts_data(request):
    if request.method == 'GET':
        year = request.GET.get('year', '2021')
        province_ = request.GET.get('province', 'Anhui')
        month = request.GET.get('month', 'January')
        month_ = month_mapping.get(month, 1)
        try:
            province = Division.objects.get(division=province_)
        except Division.DoesNotExist:
            return JsonResponse({'error': 'Province not found'}, status=404)

        filters = {
            'division': province,
            'date__year': year,
            'date__month': month_
        }

        cases, total_new_cases = new_cases(filters)

        response_data = {
            'cases': cases,
            'year': year,
            'province': province_,
            'total': total_new_cases,

        }

        return JsonResponse(response_data)

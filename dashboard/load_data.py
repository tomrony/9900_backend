import csv
from django.core.management.base import BaseCommand
from dashboard.models import Pangolin, Location, Division, GISAID

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        file = kwargs['csv_file']
        with open(file, mode='r') as f:
            r = csv.DictReader(f)
            for line in r:
                pangolin, created = Pangolin.objects.get_or_create(pangolin=line['pangolin_lineage'])
                location, created = Location.objects.get_or_create(location=line['location'])
                division, created = Division.objects.get_or_create(division=line['division'])
                GISAID.objects.create(
                    ei=line['gisaid_epi_isl'],
                    division=division,
                    location=location,
                    pangolin=pangolin,
                    date=line['date_submitted']
                )

        self.stdout.write(self.style.SUCCESS('Data successfullwy loaded'))
import csv
from django.core.management.base import BaseCommand
from dashboard.models import Pangolin, Location, Division, GISAID

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file_path = '/Users/tristam/PycharmProjects/comp9900/dashboard/management/commands/data/tsv/pp_data.csv'

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                division, _ = Division.objects.get_or_create(division=row['division'])
                location, _ = Location.objects.get_or_create(location=row['location'])
                pangolin, _ = Pangolin.objects.get_or_create(pangolin=row['pangolin_lineage'])

                GISAID.objects.create(
                    ei=row['gisaid_epi_isl'],
                    division=division,
                    location=location,
                    pangolin=pangolin,
                    date=row['date_submitted']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
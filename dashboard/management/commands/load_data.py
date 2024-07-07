import csv
from django.core.management.base import BaseCommand
from dashboard.models import Pangolin, Location, Division, GISAID
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file_path = '/Users/tristam/PycharmProjects/comp9900/dashboard/management/commands/data/tsv/pp_data.csv'

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['date'] == 'date':
                    continue
                division, _ = Division.objects.get_or_create(division=row['division'])
                location, _ = Location.objects.get_or_create(location=row['location'])
                pangolin, _ = Pangolin.objects.get_or_create(pangolin=row['pangolin_lineage'])

                date_str = row['date']
                if len(date_str) == 4:
                    year = int(date_str)
                    if year == 2019:
                        date_str = f"{date_str}-12-31"
                    elif year == 2024:
                        date_str = f"{date_str}-01-31"
                    else:
                        date_str = f"{date_str}-06-01"
                elif len(date_str) == 7:
                        date_str = f"{date_str}-01"

                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    self.stderr.write(self.style.ERROR(f"Invalid date format: {row['date']}"))
                    continue

                GISAID.objects.create(
                        ei=row['gisaid_epi_isl'],
                        division=division,
                        location=location,
                        pangolin=pangolin,
                        date=date
                    )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
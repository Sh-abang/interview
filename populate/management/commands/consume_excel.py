from datetime import datetime
import pandas as pd
from django.core.management.base import BaseCommand
from populate.models import CustUsers

class Command(BaseCommand):

    help = 'Import data from Excel file to Customer model'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']

        try:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(excel_file_path)

            


            # Iterate through rows and create Customer objects
            for index, row in df.iterrows():
                date_str = row['Date of Appointment']
                formatted_date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
                CustUsers.objects.create(
                    id_number=row['Identity Number'],
                    email=row['Email'],
                    mobile_number=row['Mobile Number'],
                    full_names=row['Full Names'],
                    designation=row['Designation'],
                    occupation=row['Occupation'],
                    Nationality=row['Nationality'],
                    income_source=row['Source of Income'],
                    res_address=row['Residential Address'],
                    post_address=row['Postal Address'],
                    
                    appoint_date=formatted_date,
                )

            self.stdout.write(self.style.SUCCESS('Data consume successful.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Data consume failed: {str(e)}'))

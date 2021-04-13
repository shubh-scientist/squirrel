from django.core.management.base import BaseCommand

import csv
  
from squitra.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')
    def handle(self, *args, **options):
        squirrel_sightings_list = Squirrel.objects.all()
        output_dict = {}
        with open(options['file'],"w") as fp:
            for item in squirrel_sightings_list:
                output_dict['X'] = item.X
                output_dict['Y'] = item.Y
                output_dict['Shift'] = item.Shift
                output_dict['Date'] = item.Date
                output_dict['Unique Squirrel ID'] = item.Unique_Squirrel_ID
                output_dict['Age'] = item.Age
                output_dict['Primary Fur Color'] = item.Primary_Fur_Color
                output_dict['Location'] = item.Location
                output_dict['Specific Location'] = item.Specific_Location
                output_dict['Running'] = item.Running
                output_dict['Chasing'] = item.Chasing
                output_dict['Climbing'] = item.Climbing
                output_dict['Eating'] = item.Eating
                output_dict['Foraging'] = item.Foraging
                output_dict['Other Activities'] = item.Other_Activities
                output_dict['Kuks'] = item.Kuks
                output_dict['Quaas'] = item.Quaas
                output_dict['Moans'] = item.Moans
                output_dict['Tail flags'] = item.Tail_flags
                output_dict['Tail twitches'] = item.Tail_twitching
                output_dict['Approaches'] = item.Approaches
                output_dict['Indifferent'] = item.Indifferent
                output_dict['Runs from'] = item.Runs_from
                output = csv.DictWriter(fp,delimiter=",",fieldnames=output_dict.keys())
                output.writeheader()
                output.writerow(output_dict)

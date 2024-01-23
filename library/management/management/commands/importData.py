# myapp/management/commands/import_books.py
import csv
from django.core.management.base import BaseCommand
from ...models import *

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('-f', type=str, help='Path to the CSV file')
        parser.add_argument('-m', type=str, help='model name')

    def handle(self, *args, **kwargs):

        file = kwargs['f']
        model = kwargs['m']
        try:
            model = eval(model)
        except:
            raise Exception("Model not found")
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Before creating the object, convert foreign key references from ids to actual objects
                foreign_key_fields = {f.name: f for f in model._meta.fields if isinstance(f, models.ForeignKey)}
                print(foreign_key_fields)
                for field_name, field in foreign_key_fields.items():
                    related_model = field.related_model
                    print("related_model", related_model)
                    if field_name in row and row[field_name]:
                        try:
                            row[field_name] = related_model.objects.get(name=row[field_name])
                        except related_model.DoesNotExist:
                            raise Exception(f"Related model for field '{field_name}' with id {row[field_name]} does not exist.")
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {model} from {file}'))

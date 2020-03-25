from django.core.management.base import BaseCommand, CommandError
from contextlib import closing
from django.db import connection
from authors.models import Authors
import timeit


def import_authors(fileName):
    try:
        with open(fileName) as authors:
            with closing(connection.cursor()) as cursor:
                cursor.copy_from(
                    file=authors,
                    table='authors_authors',
                    sep=',',
                    columns=['name']
                )

    except CommandError:
        raise CommandError('Occurred an error in the insertion')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('fileName', type=str)

    def handle(self, *args, **options):
        import_authors(options['fileName'])
        self.stdout.write(
            self.style.SUCCESS('Successfully load authors in base'),
            ending=''
        )

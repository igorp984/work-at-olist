from io import StringIO
from django.core.management import call_command
from django.test import TestCase


# Create your tests here.


class ImportAuthorsTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('import_authors', 'authors.csv', stdout=out)
        self.assertIn('Successfully load authors in base', out.getvalue())

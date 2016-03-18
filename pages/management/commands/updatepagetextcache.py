from django.core.management.base import BaseCommand, CommandError
from pages.models import PageText
from django.db.transaction import atomic

class Command(BaseCommand):
    help = 'Refreshes the text_html of every PageText'

    def add_arguments(self, parser):
        pass

    @atomic
    def handle(self, *args, **options):
        texts = PageText.objects.all()
        for pagetext in texts:
            pagetext.save() # pre_save signal does the changes

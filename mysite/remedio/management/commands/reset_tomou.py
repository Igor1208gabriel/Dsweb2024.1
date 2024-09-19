from django.core.management.base import BaseCommand
from remedio.models import Remedio

class Command(BaseCommand):
    help = 'Reseta a variável tomou para False diariamente.'

    def handle(self, *args, **kwargs):
        remedio = Remedio.objects.first()
        remedio.tomou = False
        remedio.save()
        self.stdout.write(self.style.SUCCESS('Status resetado para False'))

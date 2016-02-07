from django.core.management.base import BaseCommand

from bitnotify.cron import cron


class Command(BaseCommand):
    help = 'Run bitnotify cron task defined in bitnotify/cron.py'

    def handle(self, *args, **options):
        cron()

import logging

from django.core.management.base import BaseCommand, CommandError

from ...importers import AdiffImporter, ImporterError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import an adiff XML file into the database'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('adiff_path')

    def handle(self, adiff_path, *args, **options):
        try:
            importer = AdiffImporter()
            diff = importer.run(adiff_path)
        except ImporterError as e:
            raise CommandError(e)

        logger.info(
            'Created {} containing {} actions.'.format(
                diff, diff.actions.count()))

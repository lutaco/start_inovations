from django.core.management.base import (
    BaseCommand, CommandError
)

from grid.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            query = Product.objects.filter(name__startswith='[test]')
            query.delete()
            self.stdout.write(
                self.style.SUCCESS('Test products succesed removed')
            )
        except Exception as err:
            raise CommandError(err)
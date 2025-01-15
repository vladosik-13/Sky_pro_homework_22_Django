# catalog/management/commands/set_product_owners.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from catalog.models import Product

class Command(BaseCommand):
    help = 'Sets the owner for existing products'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        first_user = User.objects.first()

        if not first_user:
            self.stdout.write(self.style.ERROR('No users found in the database. Please create a user first.'))
            return

        # Устанавливаем владельца для всех продуктов, у которых еще нет владельца
        updated_count = Product.objects.filter(owner__isnull=True).update(owner=first_user)
        self.stdout.write(self.style.SUCCESS(f'Successfully set owner for {updated_count} products'))
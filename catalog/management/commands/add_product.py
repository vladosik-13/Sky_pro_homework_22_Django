from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Adds a new product to the database"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(
            name="Category 1", description="Category 1"
        )

        # Список продуктов
        products = [
            {
                "name": "Product 1",
                "description": "Product 1",
                "price": 100,
            },
            {
                "name": "Product 2",
                "description": "Product 2",
                "price": 200,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data["name"],
                defaults={
                    "description": product_data["description"],
                    "price": product_data["price"],
                    "category": category,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully added product: {product_data["name"]}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Product already exists: {product_data["name"]}'
                    )
                )

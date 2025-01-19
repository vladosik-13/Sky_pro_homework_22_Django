from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = "Creates groups with custom permissions for products"

    def handle(self, *args, **kwargs):
        # Получаем ContentType для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Создаем группы
        editors_group, created = Group.objects.get_or_create(name="Editors")
        moderators_group, created = Group.objects.get_or_create(name="Moderators")

        # Получаем кастомное право can_unpublish_product
        can_unpublish_permission, created = Permission.objects.get_or_create(
            codename="can_unpublish_product",
            name="может отменять публикацию продукта",
            content_type=content_type,
        )

        # Назначаем право группам
        editors_group.permissions.add(can_unpublish_permission)
        moderators_group.permissions.add(can_unpublish_permission)

        self.stdout.write(
            self.style.SUCCESS("Successfully created groups with custom permissions")
        )

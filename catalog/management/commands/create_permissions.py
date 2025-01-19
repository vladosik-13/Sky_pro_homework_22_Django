from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Creates custom permissions for products'

    def handle(self, *args, **kwargs):
        # Получаем ContentType для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Удаляем существующие права
        Permission.objects.filter(content_type=content_type).delete()

        # Создаем права
        can_unpublish_permission, created = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type
        )

        delete_permission, created = Permission.objects.get_or_create(
            codename='delete_product',
            name='Может удалять продукт',
            content_type=content_type
        )

        change_permission, created = Permission.objects.get_or_create(
            codename='change_product',
            name='Может изменять продукт',
            content_type=content_type
        )

        # Создаем группы
        editors_group, created = Group.objects.get_or_create(name='Editors')
        moderators_group, created = Group.objects.get_or_create(name='Moderators')

        # Назначаем права группам
        editors_group.permissions.add(can_unpublish_permission, change_permission)
        moderators_group.permissions.add(can_unpublish_permission, delete_permission, change_permission)

        self.stdout.write(self.style.SUCCESS('Successfully created custom permissions and assigned them to groups'))
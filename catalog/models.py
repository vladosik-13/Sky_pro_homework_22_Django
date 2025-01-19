from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="catalog/images/",
        verbose_name="фотография продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, verbose_name="цена"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="опубликован",
        help_text="Укажите, опубликован ли продукт",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        related_name="products",
    )

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        null=True, blank=True, verbose_name="описание категории"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

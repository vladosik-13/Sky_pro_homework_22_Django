from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(
        upload_to="catalog/images/",
        verbose_name="фотография продукта",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        ordering = ['-created_at']

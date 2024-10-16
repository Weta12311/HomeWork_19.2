from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="Product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="Продукты",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену продукта")
    create_date = models.DateField(
        blank=True, null=True, verbose_name="Дата создания записи"
    )
    changes_date = models.DateField(
        blank=True, null=True, verbose_name="Дата изменения записи"
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.SET_NULL)

    status = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "create_date", "changes_date"]
        permissions = [
            ('can_change_product_status', 'can change product status'),
            ('can_change_description', 'can change description'),
            ('can_change_category', 'can change category')
        ]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи",
    )
    text = models.TextField(
        verbose_name="Текст статьи", help_text="Введите текст статьи"
    )
    image = models.ImageField(
        upload_to="Blog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.CharField(
        verbose_name="Признак публикации",
        help_text="Введите признак публикации",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        blank=True, null=True, verbose_name="Дата создания записи"
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата изменения записи"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title", "category", "created_at", "updated_at"]

    def __str__(self):
        return self.title


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name="Продукт",
        blank=True,
        null=True,
        related_name="version",)
    version_number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    version_sign = models.BooleanField(default=False, verbose_name='признак версии')

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "version_number", "name", "version_sign"]

    def __str__(self):
        return f'{self.name} - {self.version_number}'

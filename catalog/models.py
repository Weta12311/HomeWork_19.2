from django.db import models
import datetime


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
        related_name='Продукты'
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену продукта")
    create_date = models.DateField(
        blank=True, null=True, verbose_name="Дата создания записи"
    )
    changes_date = models.DateField(
        blank=True, null=True, verbose_name="Дата изменения записи"
    )
    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "create_date", "changes_date"]

    def __str__(self):
        return self.name




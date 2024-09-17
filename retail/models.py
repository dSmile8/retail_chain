from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Chain(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя звена")
    contacts = models.ForeignKey('Contact', on_delete=models.CASCADE, verbose_name="Контакты", **NULLABLE)
    products = models.ManyToManyField('Product')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность',
                                           **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Звено'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=30, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return f'{self.title} ({self.model})'

    class Meta:
        verbose_name_plural = 'Продукт'


class Contact(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE, verbose_name='Звено', **NULLABLE),
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.country} ({self.city}) - {self.street}: {self.house_number}'

    class Meta:
        verbose_name_plural = 'контакты'

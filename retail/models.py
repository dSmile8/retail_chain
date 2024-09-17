from django.db import models

NULLABLE = {'blank': True, 'null': True}

CHOICES = (
    ('Завод', 'Завод изготовитель'),
    ('Сеть', 'Торговая сеть'),
    ('ИП', 'Индивидуальный предприниматель'),
)


class Chain(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя звена")
    contacts = models.ForeignKey('Contact', on_delete=models.CASCADE, verbose_name="Контакты",
                                 **NULLABLE)
    products = models.ManyToManyField('Product')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность',
                                           **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_factory = models.BooleanField(default=False, verbose_name='Завод')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # у завода не может быть поставщиков
        if self.is_factory:
            self.parent = None
        super().save(*args, **kwargs)

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
    chain_line = models.CharField(max_length=20, verbose_name='Звено в цепи', choices=CHOICES, **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.chain_line}/{self.country} ({self.city}) - {self.street}: {self.house_number}'

    class Meta:
        verbose_name_plural = 'контакты'

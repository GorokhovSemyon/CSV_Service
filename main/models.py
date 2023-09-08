from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

SERVICES = [
    ('cut1', 'cut1'),
    ('cut2', 'cut2'),
    ('cut3', 'cut3'),
    ('cut4', 'cut4'),
    ('cut5', 'cut5'),
    ('beard1', 'beard1'),
    ('beard2', 'beard2'),
    ('beard3', 'beard3'),
    ('beard4', 'beard4'),
    ('style1', 'style1'),
    ('style2', 'style2'),
    ('style3', 'style3'),
    ('style4', 'style4'),
    ('style5', 'style5'),
    ('style6', 'style6'),
    ]
MASTERS = [
    ('Master1', 'Master1'),
    ('Master2', 'Master2'),
    ('Master3', 'Master3'),
]

TIMES = [
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:30', '15:30'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('18:45', '18:45'),
    ('19:30', '19:30'),

]
class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    order_phone = models.CharField(validators=[phone_regex], max_length=16, verbose_name='Номер')
    order_email = models.EmailField(max_length=70, blank=True, unique=True, verbose_name='Почта')
    services = models.CharField(max_length=20, null=True, choices=SERVICES, verbose_name="Услуги")
    Master = models.CharField(max_length=20, null=True, choices=MASTERS, verbose_name="Мастер")
    Date =  models.CharField(max_length=20, null=True, verbose_name="Дата")
    Time = models.CharField(max_length=20, null=True, choices=TIMES, verbose_name="Время")
    def __str__(self):
        return f"{self.order_name}"
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    objects = models.Manager()
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, default='')

    def __str__(self):
        return self.email

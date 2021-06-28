from django.db import models
from django.db.models import IntegerField, Model
from django import forms
from django.utils import timezone
from django.utils.timezone import now
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Questions(models.Model):
    question = models.CharField(verbose_name=_('Вопрос'), max_length=1000)
    answer = models.TextField(verbose_name=_('Ответ'))

    def __str__(self, *args, **kwargs):
        return _("Вопрос: %s") % (self.question)

    class Meta:
        verbose_name = _('Частый вопрос')
        verbose_name_plural = _('Частые вопросы')

class Drivers(models.Model):
    name = models.CharField(verbose_name=_('Имя водителя'), max_length=100)
    phone = models.CharField('Телефон', blank=True, null=True, max_length = 25)
    email = models.EmailField('Email водителя', blank=True, null=True)
    car = models.CharField(verbose_name=_('Марка автомобиля'), max_length=100)


    def __str__(self, *args, **kwargs):
        return "Водитель: %s" % (self.name)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Status(models.Model):
    name = models.CharField(verbose_name=_('Статус'), max_length=100)


    def __str__(self, *args, **kwargs):
        return "Статус: %s" % (self.name)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

class StatusPay(models.Model):
    name = models.CharField(verbose_name=_('Метод оплаты'), max_length=100)

    def __str__(self, *args, **kwargs):
        return "Метод: %s" % (self.name)

    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'

class Car(models.Model):
    pictureCar = models.ImageField(verbose_name=_('Фото машины'), upload_to='cars_images/')
    modelsOfCars = models.CharField(verbose_name=_('Модель'), max_length=300)
    classOfCars = models.CharField(verbose_name=_('Класс трансфера'), max_length=100)
    infoOfClass = models.CharField(verbose_name=_('Информация о классе'), max_length=300)
    maxPassenger = models.IntegerField(verbose_name=_('Максимальное кол-во пассажиров'))
    maxBags = models.IntegerField(verbose_name=_('Максимальное кол-во багажного места'))
    priceOfTransfer = models.FloatField(verbose_name=_('Коэффициент трансфера'), blank=True, null=True)

    def __str__(self, *args, **kwargs):
        return "Класс трансфера: %s №%s " % (self.classOfCars, str(self.id))

    class Meta:
        verbose_name = 'Класс трансфера'
        verbose_name_plural = 'Классы трансферов'


# Класс формы обратной связи заказа трансфера
class Order(models.Model):
    from_transfer = models.CharField('Откуда', max_length=128)
    time_from = models.CharField('Дата отправления и время', max_length=128)
    to_transfer = models.CharField('Куда', max_length=128)
    class_transport = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=u'Класс транспорта')
    passenger = models.IntegerField('Кол-во пассажиров',
    default=1
        # max_value = 4
    )
    children = models.BooleanField('Есть-ли дети')
    return_transfer = models.BooleanField('Есть-ли обратный трансфер')
    time_return_transfer = models.CharField('Время обратного трансфера', blank=True, null=True, max_length=128)
    children_passenger = models.IntegerField('Кол-во детей', blank=True, null=True)
    chair_small = models.IntegerField('0-13 кг', default=0, blank=True, null=True)
    chair_middle = models.IntegerField('9-18 кг', default=0, blank=True, null=True)
    chair_large = models.IntegerField('15-36 кг', default=0, blank=True, null=True)
    name = models.CharField('Имя клиента', max_length=128)
    email = models.EmailField('Email клиента')
    phone = models.CharField('Телефон', max_length = 18)
    comment = models.TextField('Комментарии', blank=True, null=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)
    status_pay = models.ForeignKey (StatusPay, on_delete=models.CASCADE, verbose_name=_('Метод оплаты'), blank=True, null=True)
    paid = models.BooleanField('Оплачен', blank=True, null=True)
    status = models.ForeignKey (Status, on_delete=models.CASCADE, null = True)
    drivers = models.ForeignKey(Drivers ,on_delete=models.CASCADE, verbose_name=u'Водитель', blank=True, null=True)
    price = models.IntegerField(verbose_name=_('Цена'), blank=True, null=True)
    price_company = models.IntegerField(verbose_name=_('Себестоимость'), blank=True, null=True)

    # def __str__(self, *args, **kwargs):
    #     return "Статус: %s" % (self.name)
    def __str__(self, *args, **kwargs):
        return "№ %s Имя: %s Дата: %s Статус: %s" % (str(self.id), self.name, str(self.created), self.status)

    def save(self, *args, **kwargs):
        if self.status is None:  # Set default reference
            self.status = Status.objects.get(id=1)

        if self.passenger > self.class_transport.maxPassenger:
            raise ValidationError("Допущено превышение пассажиров")

        super(Order, self).save(*args, **kwargs)
        # super(Order, self).save(*args, **kwargs)
    #     return super(Order, self).clean()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

from django.db import models
from django.utils import timezone


class Branch(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name


class Locomotive(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Локомотив'
        verbose_name_plural = 'Локомотивы'

    def __str__(self):
        return self.name


class Period(models.Model):
    year = models.IntegerField(default=2017)
    run = models.IntegerField(default=0)
    branch = models.ForeignKey('Branch', default=0, on_delete=True)
    locomotive = models.ForeignKey('Locomotive', on_delete=True, default=0)

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    def __str__(self):
        return str(self.year)

    # #####
    # from django.db import models
    # from django.utils import timezone
    #
    # # Create your models here.
    # # from otdels.models import Otdel
    #
    # class Worker(models.Model):
    #     name = models.CharField('Имя', max_length=100)
    #     fname = models.CharField('Фамилия', max_length=100)
    #     status = models.IntegerField(choices=((0, 'new'), (1, 'work'), (2, 'deleled')))
    #     # status = models.IntegerField(choices=)
    #     create_date = models.DateTimeField('Дата создания', default=timezone.now)
    #     balance = models.FloatField('Баланс денег', default=0)
    #     otdel = models.ForeignKey('otdels.Otdel', default=0)  #
    #
    #     # otd = Otdel()
    #
    #     class Meta:
    #         """Служит для перевода класса Post"""
    #         verbose_name = 'Рабочий'
    #         verbose_name_plural = 'Рабочие'
    #
    #     def __str__(self):
    #         return '{} {}'.format(self.name, self.fname)
    #
    #     def __del__(self):
    #         pass
    #
    # class Contact(models.Model):
    #     type_contact = models.IntegerField('Тип контакта (телефон / e-mail)', choices=((0, 'phone'), (1, 'e-mail')))
    #     contact = models.CharField('Контакт', max_length=256)
    #     worker = models.ForeignKey('Worker')
    #
    #     class Meta:
    #         verbose_name = 'Контакт'
    #         verbose_name_plural = 'Контакты'
    #
    #     def __str__(self):
    #         return '{} {}'.format(self.worker, self.contact)
    #
    # class Adress(models.Model):
    #     indx = models.IntegerField('Индекс')
    #     region = models.CharField('Регион проживания', max_length=50)
    #     sity = models.CharField('Город проживания', max_length=50)
    #     street = models.CharField('Улица', max_length=50)
    #     home = models.CharField('Дом', max_length=9999)
    #     flat = models.IntegerField('Квартира')
    #     worker = models.ForeignKey('Worker')
    #
    #     class Meta:
    #         verbose_name = 'Адрес'
    #         verbose_name_plural = 'Адреса'
    #
    #     def __str__(self):
    #         return 'Домашний адрес: {}, {}, {}, {}, {}, {}'.format(self.indx, self.region, self.sity, self.street,
    #                                                                self.home,
    #                                                                self.flat)

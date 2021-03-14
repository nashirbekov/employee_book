# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class City(models.Model):
    """Города"""
    name = models.CharField("Город", unique=True, max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class WorkStatus(models.Model):
    """Статус работы"""
    status = models.CharField("Статус", max_length=150)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус работы"
        verbose_name_plural = "Статусы работы"


class Employee(models.Model):
    """Сотрудник"""
    g_choice = (
        ('М', 'Мужской'),
        ('Ж', 'Женский')

    )
    lastname = models.CharField("Фамилия", max_length=150)
    firstname = models.CharField("Имя", max_length=150)
    middlename = models.CharField("Отчество", max_length=150, blank=True, null=True)
    image = models.ImageField("Фото", upload_to="employees/")
    phone_number = models.CharField("Номер телефона", max_length=14, default="+996 ")
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.SET_NULL, null=True)
    age = models.PositiveSmallIntegerField("Возраст")
    gender = models.CharField("Пол", choices=g_choice, max_length=10)
    email = models.EmailField("Email")
    work_status = models.ForeignKey(WorkStatus, verbose_name="Статус работы", on_delete=models.SET_NULL, null=True)
    employment_date = models.DateField("Дата приема на работу")
    date_of_dismissal = models.DateField("Дата увольнения", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"






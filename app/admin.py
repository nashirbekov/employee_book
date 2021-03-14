# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import Employee, City, WorkStatus

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Сотрудник"""

    list_display = ("lastname", "firstname", "middlename", "phone_number", "age", "gender", "email", "user")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Город"""
    list_display = ("name",)

@admin.register(WorkStatus)
class WorkStatusAdmin(admin.ModelAdmin):
    """Статус работы"""
    short_description = "Статусы работы"
    list_display = ("status",)

# Generated by Django 3.1.7 on 2021-03-13 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='WorkStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=150, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус работы',
                'verbose_name_plural': 'Статусы работы',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=150, verbose_name='Имя')),
                ('middlename', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('image', models.ImageField(upload_to='employees/', verbose_name='Фото')),
                ('phone_number', models.CharField(default='+996 ', max_length=14, verbose_name='Номер телефона')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(max_length=100, verbose_name='Пол')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('employment_date', models.DateField(verbose_name='Дата приема на работу')),
                ('date_of_dismissal', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.city', verbose_name='Город')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.workstatus', verbose_name='Статус работы')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]

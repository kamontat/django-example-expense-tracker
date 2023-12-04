# Generated by Django 4.2.8 on 2023-12-04 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(2)])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=999999999.99)),
            ],
        ),
    ]

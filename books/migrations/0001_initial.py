# Generated by Django 3.2.8 on 2021-10-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Kitobni nomi')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Kitobni subtitle')),
                ('author', models.CharField(max_length=200, verbose_name='Kitobni aftori')),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
# Generated by Django 5.1.4 on 2025-02-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reformas_ejer09', '0008_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]

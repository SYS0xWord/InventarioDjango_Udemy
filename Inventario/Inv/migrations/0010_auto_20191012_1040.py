# Generated by Django 2.2.2 on 2019-10-12 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0009_auto_20190923_1741'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('codigo', 'descripcion', 'unidad_medida', 'subcategoria', 'marca')},
        ),
    ]

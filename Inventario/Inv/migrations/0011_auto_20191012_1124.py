# Generated by Django 2.2.2 on 2019-10-12 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0010_auto_20191012_1040'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('descripcion', 'unidad_medida', 'subcategoria', 'marca')},
        ),
    ]

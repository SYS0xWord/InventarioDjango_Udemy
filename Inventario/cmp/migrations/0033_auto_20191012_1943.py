# Generated by Django 2.2.2 on 2019-10-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0032_auto_20191007_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='precio_unitario',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro_lote',
            name='precio_unitario',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]

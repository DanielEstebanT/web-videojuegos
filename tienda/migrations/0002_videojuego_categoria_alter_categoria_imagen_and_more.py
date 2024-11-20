# Generated by Django 5.1.2 on 2024-11-20 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_categorias', to='tienda.categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='categorias/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='imagen',
            field=models.ImageField(null=True, upload_to='videojuegos/', verbose_name='Imagen'),
        ),
    ]

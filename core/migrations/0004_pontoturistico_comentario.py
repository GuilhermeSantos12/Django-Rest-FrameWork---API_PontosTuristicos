# Generated by Django 3.2.4 on 2021-06-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.Comentarios'),
        ),
    ]

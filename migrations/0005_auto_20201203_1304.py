# Generated by Django 3.1.3 on 2020-12-03 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('immobapp', '0004_auto_20201202_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immobilier',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immobapp.ville', verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='picture_one',
            field=models.ImageField(upload_to='immobapp/static/immobapp/images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='picture_three',
            field=models.ImageField(blank=True, default=1, upload_to='immobapp/static/immobapp/images/', verbose_name='image 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='picture_two',
            field=models.ImageField(blank=True, default=1, upload_to='immobapp/static/immobapp/images/', verbose_name='image 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='status',
            field=models.CharField(max_length=128, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='types',
            field=models.CharField(max_length=128, verbose_name='Type'),
        ),
    ]

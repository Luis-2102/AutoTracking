# Generated by Django 5.0.2 on 2024-02-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about_imgp_about_user_contacto_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lenguaje',
            name='about',
        ),
        migrations.RemoveField(
            model_name='lenguaje',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='especialidad',
            options={'ordering': ['-created'], 'verbose_name': 'Sub-Titulo', 'verbose_name_plural': 'Sub-Titulos'},
        ),
        migrations.AlterModelOptions(
            name='portafolio',
            options={'ordering': ['-created'], 'verbose_name': 'Vehículo', 'verbose_name_plural': 'Vehículos'},
        ),
        migrations.RemoveField(
            model_name='about',
            name='Tit',
        ),
        migrations.RemoveField(
            model_name='about',
            name='imgp',
        ),
        migrations.RemoveField(
            model_name='about',
            name='user',
        ),
        migrations.RemoveField(
            model_name='especialidad',
            name='user',
        ),
        migrations.RemoveField(
            model_name='portafolio',
            name='url',
        ),
        migrations.RemoveField(
            model_name='portafolio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='user',
        ),
        migrations.AlterField(
            model_name='about',
            name='perfil',
            field=models.CharField(max_length=100, verbose_name='Cedula'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='Espe',
            field=models.CharField(max_length=100, verbose_name='Sub-Titulo'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de adquisión'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='img1',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Imagen 1'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='img2',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='img3',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Imagen 3'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nombre Vehiculo'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='tipo',
            field=models.CharField(max_length=100, verbose_name='Tipo/Marca del Vehiculo'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='svc',
            field=models.CharField(max_length=150, verbose_name='Titulo'),
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.DeleteModel(
            name='Lenguaje',
        ),
    ]

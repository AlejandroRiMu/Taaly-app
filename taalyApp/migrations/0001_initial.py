# Generated by Django 4.1.1 on 2022-11-26 23:51

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('efectos', models.CharField(max_length=30)),
                ('usos', models.CharField(max_length=30)),
            ],
        ),
    ]
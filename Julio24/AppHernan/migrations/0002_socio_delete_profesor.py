# Generated by Django 5.0.6 on 2024-07-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHernan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]

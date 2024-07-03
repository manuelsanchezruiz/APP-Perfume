# Generated by Django 5.0.6 on 2024-06-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
    ]

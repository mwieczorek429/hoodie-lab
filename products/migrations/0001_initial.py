# Generated by Django 5.0.2 on 2024-03-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hoodie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=300)),
                ('category', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avaiable', models.BooleanField(default=True)),
            ],
        ),
    ]
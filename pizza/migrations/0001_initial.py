# Generated by Django 3.1.4 on 2020-12-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Regular', 'Regular'), ('Square', 'Square')], default=('Regular', 'Regular'), max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('toppings', models.ManyToManyField(blank=True, to='pizza.Topping')),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-23 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('happy', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='form.Product')),
            ],
        ),
    ]

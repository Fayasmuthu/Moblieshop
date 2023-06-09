# Generated by Django 4.2.1 on 2023-06-01 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_latesta_latestb_teamoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField()),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

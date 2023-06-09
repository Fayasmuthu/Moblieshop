# Generated by Django 4.2.1 on 2023-06-01 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='media/order')),
                ('qunatity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.order')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-14 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211114_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='receipt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.receipt'),
        ),
    ]

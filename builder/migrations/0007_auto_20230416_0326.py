# Generated by Django 3.0.2 on 2023-04-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_auto_20230416_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Block_chin_blockNo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='trans_detial',
            field=models.CharField(default='trans', max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.15 on 2023-04-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portFolioApp', '0002_auto_20230422_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioimage',
            name='image',
            field=models.ImageField(upload_to='portfolio_images/'),
        ),
    ]

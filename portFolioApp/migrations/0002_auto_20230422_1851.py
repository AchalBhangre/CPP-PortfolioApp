# Generated by Django 2.1.15 on 2023-04-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portFolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioimage',
            name='image',
            field=models.ImageField(upload_to='media/portfolio_images/'),
        ),
    ]

# Generated by Django 2.1.15 on 2023-04-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portFolioApp', '0003_auto_20230422_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioregistration',
            name='portfolio_images',
            field=models.ManyToManyField(blank=True, related_name='registrations', to='portFolioApp.PortfolioImage'),
        ),
    ]

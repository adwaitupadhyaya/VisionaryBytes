# Generated by Django 4.2.1 on 2023-07-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0012_clientrequestsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequestsmodel',
            name='technician',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
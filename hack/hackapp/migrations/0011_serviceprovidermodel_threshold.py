# Generated by Django 4.2.1 on 2023-07-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0010_alter_serviceprovidermodel_citizenship_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovidermodel',
            name='threshold',
            field=models.FloatField(blank='True', default=0, null=True),
        ),
    ]

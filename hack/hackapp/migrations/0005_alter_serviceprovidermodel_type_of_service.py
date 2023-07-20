# Generated by Django 4.2.1 on 2023-07-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0004_serviceprovidermodel_type_of_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovidermodel',
            name='type_of_service',
            field=models.CharField(blank=True, choices=[('Electrician', 'electrician'), ('IT', 'IT'), ('Plumbing', 'Plumbing'), ('Gardening', 'Gardening'), ('Painting', 'Painting'), ('Carpentry', 'Carpentry')], max_length=20, null=True),
        ),
    ]

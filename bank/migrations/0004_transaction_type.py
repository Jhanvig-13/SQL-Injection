# Generated by Django 4.2.1 on 2023-05-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_transaction_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

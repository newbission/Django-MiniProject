# Generated by Django 5.1 on 2024-08-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_alter_transaction_trans_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="trans_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="trans_time",
            field=models.TimeField(),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailer", "0005_id_bigautofield"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="retry_count",
            field=models.IntegerField(default=0),
        ),
    ]
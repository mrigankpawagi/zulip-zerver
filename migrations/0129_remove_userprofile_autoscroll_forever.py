# Generated by Django 1.11.6 on 2017-12-27 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0128_scheduledemail_realm"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="autoscroll_forever",
        ),
    ]

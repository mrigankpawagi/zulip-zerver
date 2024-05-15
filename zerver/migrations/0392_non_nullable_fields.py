# Generated by Django 3.2.12 on 2022-04-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0391_alter_stream_history_public_to_subscribers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customprofilefield",
            name="field_data",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="customprofilefield",
            name="hint",
            field=models.CharField(default="", max_length=80),
        ),
        migrations.AlterField(
            model_name="realmuserdefault",
            name="enter_sends",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="stream",
            name="invite_only",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="is_muted",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="enter_sends",
            field=models.BooleanField(default=False),
        ),
    ]
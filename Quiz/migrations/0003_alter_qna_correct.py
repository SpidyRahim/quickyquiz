# Generated by Django 4.1 on 2022-10-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Quiz", "0002_create"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qna", name="Correct", field=models.CharField(max_length=10),
        ),
    ]

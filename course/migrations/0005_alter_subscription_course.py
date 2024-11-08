# Generated by Django 4.2 on 2024-11-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="course.course",
                verbose_name="курс",
            ),
        ),
    ]

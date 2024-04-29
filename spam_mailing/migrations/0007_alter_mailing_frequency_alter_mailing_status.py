# Generated by Django 4.2.6 on 2024-04-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spam_mailing", "0006_alter_mailing_send_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("ежедневно", "Раз в день"),
                    ("еженедельно", "Раз в неделю"),
                    ("ежемесячно", "Раз в месяц"),
                ],
                max_length=15,
                verbose_name="Рассылка",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("создана", "Создана"),
                    ("запущена", "Запущена"),
                    ("завершена", "Завершена"),
                ],
                max_length=10,
                verbose_name="Статус",
            ),
        ),
    ]
# Generated by Django 4.2.6 on 2024-04-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spam_mailing", "0002_alter_client_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("send_time", models.DateTimeField(verbose_name="Время отправки")),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("daily", "Раз в день"),
                            ("weekly", "Раз в неделю"),
                            ("monthly", "Раз в месяц"),
                        ],
                        max_length=10,
                        verbose_name="Рассылка",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("started", "Запущена"),
                            ("completed", "Завершена"),
                        ],
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(
                        to="spam_mailing.client", verbose_name="Клиенты"
                    ),
                ),
            ],
        ),
    ]

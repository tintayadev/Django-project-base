# Generated by Django 3.2.25 on 2024-06-28 10:57

from django.db import migrations, models
import django.db.models.deletion
import item.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=item.models.item_image_file_path,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="Maximum 999.99",
                        max_digits=5,
                        verbose_name="price",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_available", models.BooleanField(default=True)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.seller"
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "ordering": ["name"],
            },
        ),
    ]

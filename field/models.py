import uuid
from django.db import models

from django_cryptography.fields import encrypt


class Field(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=50)

    sensitive_data = encrypt(models.CharField(max_length=50))


class FieldDetails(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.PROTECT,
        db_column='detail_field',
        related_name='details',
        blank=True,
        null=True
    )

    detail_sensitive_data = encrypt(models.CharField(max_length=50))

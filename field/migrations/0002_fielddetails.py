# Generated by Django 3.2.13 on 2022-05-25 03:07

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('detail_sensitive_data', django_cryptography.fields.encrypt(models.CharField(max_length=50))),
                ('field', models.ForeignKey(blank=True, db_column='field', null=True, on_delete=django.db.models.deletion.PROTECT, to='field.field')),
            ],
        ),
    ]

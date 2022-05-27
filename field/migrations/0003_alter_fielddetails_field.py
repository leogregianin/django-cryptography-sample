# Generated by Django 3.2.13 on 2022-05-25 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0002_fielddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fielddetails',
            name='field',
            field=models.ForeignKey(blank=True, db_column='detail_field', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='details', to='field.field'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-29 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meet.location'),
            preserve_default=False,
        ),
    ]
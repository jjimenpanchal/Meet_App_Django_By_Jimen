# Generated by Django 3.2.4 on 2021-06-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0005_auto_20210630_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='date',
            field=models.DateField(default='2021-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meet',
            name='organizer_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]

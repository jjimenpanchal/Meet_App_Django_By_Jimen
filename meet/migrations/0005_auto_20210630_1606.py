# Generated by Django 3.2.4 on 2021-06-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0004_meet_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meet',
            name='Participants',
            field=models.ManyToManyField(blank=True, null=True, to='meet.Participant'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pakidex', '0002_rename_pakiname_card_personalname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='whoseDeck',
        ),
        migrations.AddField(
            model_name='deck',
            name='whoseCard',
            field=models.ManyToManyField(to='pakidex.card'),
        ),
    ]
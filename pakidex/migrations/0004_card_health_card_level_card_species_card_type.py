# Generated by Django 4.0.3 on 2022-05-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pakidex', '0003_remove_card_whosedeck_deck_whosecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='health',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='card',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='card',
            name='species',
            field=models.CharField(choices=[('bulb', 'Bulbasaur'), ('sqrt', 'Squirtle'), ('char', 'Charmander'), ('pika', 'Pikachu'), ('pigy', 'Pidgey'), ('geod', 'Geodude'), ('vanil', 'Vanillite')], default='bulb', max_length=280),
        ),
        migrations.AddField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('gr', 'Grass'), ('h20', 'Water'), ('fr', 'Fire'), ('ic', 'Ice'), ('fy', 'Flying'), ('ro', 'Rock'), ('ec', 'Electric')], default='gr', max_length=12),
        ),
    ]

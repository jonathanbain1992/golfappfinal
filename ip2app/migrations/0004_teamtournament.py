# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ip2app', '0003_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournamentName', models.CharField(max_length=200)),
                ('GolfTeams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ip2app.GolfTeam')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ip2app.Tournament')),
            ],
        ),
    ]

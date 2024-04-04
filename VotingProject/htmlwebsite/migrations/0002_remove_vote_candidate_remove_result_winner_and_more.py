# Generated by Django 5.0.3 on 2024-04-03 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='result',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='election',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='result',
            name='election',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='election',
        ),
        migrations.DeleteModel(
            name='StudentDetails',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='user',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='Election',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.DeleteModel(
            name='Voter',
        ),
    ]
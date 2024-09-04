# Generated by Django 5.0.7 on 2024-09-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_language_technology_mission_personal_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='mission',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name_plural': 'Technologies'},
        ),
        migrations.RenameField(
            model_name='mission',
            old_name='language_a',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='mission',
            old_name='stack_a',
            new_name='stack',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='language_b',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='stack_b',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='stack_c',
        ),
        migrations.AlterField(
            model_name='mission',
            name='daily_rate',
            field=models.IntegerField(error_messages={'invalid': 'Doit être un nombre entier compris entre 100 et 2000'}),
        ),
        migrations.AlterField(
            model_name='mission',
            name='description',
            field=models.TextField(error_messages={'invalid': 'Doit faire moins de 1000 caractères'}, max_length=1000),
        ),
        migrations.AlterField(
            model_name='mission',
            name='duration',
            field=models.IntegerField(error_messages={'invalid': 'Doit être un nombre entier compris entre 1 et 1000'}),
        ),
        migrations.AlterField(
            model_name='mission',
            name='experience_level',
            field=models.IntegerField(error_messages={'invalid': 'Doit être un nombre entier compris entre 1 et 40'}),
        ),
    ]

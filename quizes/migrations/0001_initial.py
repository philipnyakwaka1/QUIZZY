# Generated by Django 5.0.6 on 2024-05-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='Duration of the quiz in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='Required score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]

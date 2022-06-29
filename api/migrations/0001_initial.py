# Generated by Django 4.0.5 on 2022-06-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlizzardToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=150)),
                ('token_type', models.CharField(max_length=150)),
                ('expires_in', models.IntegerField()),
            ],
        ),
    ]
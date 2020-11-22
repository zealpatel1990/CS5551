# Generated by Django 3.1.1 on 2020-11-22 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=255)),
                ('game_object', models.TextField()),
                ('player1_username', models.CharField(max_length=255)),
                ('player2_username', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_open_to_join', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkers', '0003_auto_20200926_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adherent',
            name='repassword',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
# Generated by Django 2.1 on 2018-09-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]

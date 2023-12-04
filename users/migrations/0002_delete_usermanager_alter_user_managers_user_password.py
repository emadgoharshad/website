# Generated by Django 4.1.1 on 2023-11-22 13:17

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserManager',
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=11228, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
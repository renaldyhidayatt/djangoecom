# Generated by Django 4.0.1 on 2022-02-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_userprofile_user'),
        ('store', '0002_auto_20210826_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account'),
        ),
    ]
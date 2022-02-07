# Generated by Django 4.0.1 on 2022-02-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_status_alter_order_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_methdo',
            new_name='payment_method',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
# Generated by Django 2.0.2 on 2018-10-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_profile_mc_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription_groups',
            field=models.ManyToManyField(blank=True, to='core.SubscriptionGroup'),
        ),
    ]

# Generated by Django 2.0.1 on 2018-06-02 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_featuredtalk'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredtalk',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='featuredtalk',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_talks', to='accounts.Profile'),
        ),
    ]
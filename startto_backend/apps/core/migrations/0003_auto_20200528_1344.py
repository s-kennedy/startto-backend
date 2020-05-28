# Generated by Django 3.0.6 on 2020-05-28 13:44

from django.db import migrations, models
import django_resized.forms
import startto_backend.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
        ('core', '0002_subscriptiongroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('submittable_id', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, max_length=200, quality=99, size=[250, 250], storage=startto_backend.storage_backends.MediaStorage(), upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Topic',
            new_name='Label',
        ),
        migrations.DeleteModel(
            name='SubscriptionGroup',
        ),
        migrations.RenameField(
            model_name='label',
            old_name='topic',
            new_name='label_text',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='province',
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='street_address',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
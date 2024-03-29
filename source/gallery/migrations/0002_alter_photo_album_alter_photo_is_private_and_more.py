# Generated by Django 4.0 on 2022-04-02 11:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.album', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='is_private',
            field=models.BooleanField(blank=True, default=False, verbose_name='Приватный?'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='accounts.profile', verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='PhotoToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.UUID('44acc622-3923-4181-816c-19a92a2da180'))),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='gallery.photo')),
            ],
        ),
    ]

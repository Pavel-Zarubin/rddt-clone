# Generated by Django 2.2 on 2019-04-23 13:22

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190423_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]

# Generated by Django 2.1 on 2018-08-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=255),
        ),
    ]
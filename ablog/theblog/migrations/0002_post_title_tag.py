# Generated by Django 4.0.5 on 2022-06-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="Matthew McDowell's Blog", max_length=255),
        ),
    ]

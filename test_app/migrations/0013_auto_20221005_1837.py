# Generated by Django 3.2 on 2022-10-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0012_auto_20221005_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='cols',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testtable',
            name='rows',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
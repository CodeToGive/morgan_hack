# Generated by Django 3.2 on 2022-10-04 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0010_auto_20221004_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtoken',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.testtable'),
        ),
    ]

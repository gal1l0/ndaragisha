# Generated by Django 2.2.2 on 2019-07-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190716_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitems',
            name='found_person_id',
            field=models.TextField(default='empty', null=True),
        ),
    ]
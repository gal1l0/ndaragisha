# Generated by Django 2.2.2 on 2019-07-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_lostitems_found_person_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundButNotAssigned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found_person', models.CharField(default='empty', max_length=120)),
                ('found_person_id', models.CharField(default='empty', max_length=12)),
                ('found_doc_id', models.CharField(default='empty', max_length=23)),
                ('found_doc_type', models.CharField(default='empty', max_length=40)),
                ('found_person_phone', models.CharField(default='empty', max_length=50)),
            ],
        ),
    ]
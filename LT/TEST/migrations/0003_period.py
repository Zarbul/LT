# Generated by Django 2.1.2 on 2018-10-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEST', '0002_auto_20181003_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2017)),
                ('run', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(default=0, on_delete=True, to='TEST.Branch')),
                ('locomotive', models.OneToOneField(default=0, on_delete=True, to='TEST.Locomotive')),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
            },
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEST', '0003_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='locomotive',
            field=models.ForeignKey(default=0, on_delete=True, to='TEST.Locomotive'),
        ),
    ]

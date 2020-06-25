# Generated by Django 3.0.7 on 2020-06-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('count', models.CharField(max_length=4)),
                ('last', models.CharField(max_length=4)),
            ],
        ),
    ]

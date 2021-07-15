# Generated by Django 2.2.5 on 2021-07-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20210715_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(to='rooms.Facility'),
        ),
        migrations.AddField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(to='rooms.Rule'),
        ),
    ]

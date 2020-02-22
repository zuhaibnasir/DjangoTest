# Generated by Django 3.0.3 on 2020-02-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
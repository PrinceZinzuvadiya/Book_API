# Generated by Django 4.2.5 on 2023-12-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('lsbn', models.BigIntegerField()),
                ('publisher', models.CharField(max_length=30)),
            ],
        ),
    ]

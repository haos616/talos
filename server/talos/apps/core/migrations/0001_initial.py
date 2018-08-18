# Generated by Django 2.0.7 on 2018-08-09 21:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('domains', models.ManyToManyField(to='core.Domain')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

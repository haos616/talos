# Generated by Django 2.0.7 on 2018-08-09 22:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_domaingroup_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='users',
            field=models.ManyToManyField(related_name='domains', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='domaingroup',
            name='domains',
            field=models.ManyToManyField(related_name='domain_groups', to='core.Domain'),
        ),
        migrations.AlterField(
            model_name='domaingroup',
            name='users',
            field=models.ManyToManyField(related_name='domain_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
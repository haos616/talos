from django.db import models
from django.contrib.auth.models import User


class DomainGroup(models.Model):
    name = models.CharField(max_length=127, unique=True)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True, db_index=True)
    domains = models.ManyToManyField('core.Domain', related_name='domain_groups')
    users = models.ManyToManyField(User, related_name='domain_groups', blank=True)

    def __str__(self):
        return f'{self.name}'


class Domain(models.Model):
    name = models.CharField(max_length=127, unique=True)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True, db_index=True)
    users = models.ManyToManyField(User, related_name='domains', blank=True)

    def __str__(self):
        return f'{self.name}'

from django.contrib import admin

from talos.apps.core.models import Domain, DomainGroup


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('active', 'domain_groups', )
    filter_horizontal = ('users', )


class DomainGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('active', 'domains', 'users', )
    filter_horizontal = ('users', 'domains', )


admin.site.register(Domain, DomainAdmin)
admin.site.register(DomainGroup, DomainGroupAdmin)

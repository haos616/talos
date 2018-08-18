from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth import _get_user_session_key as get_user_session_key, SESSION_KEY

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission

from talos.apps.core.models import Domain


class DomainPermission(BasePermission):
    """
    Domain permission
    """
    message = "Not permission for this domain"

    def has_permission(self, request, view):
        original_host = request.META.get('HTTP_X_ORIGINAL_HOST')
        user = request.user

        result = False
        if original_host and user.is_active:
            if user.is_superuser:
                result = True
            else:
                result = (
                    Domain.objects.filter(
                        Q(users__pk=user.pk) |
                        Q(domain_groups__users__pk=user.pk, domain_groups__active=True),
                        name__iexact=original_host,
                        active=True
                    ).exists()
                )
        return result


class AuthApiView(APIView):
    permission_classes = (IsAuthenticated, DomainPermission, )

    def get(self, request, format=None):
        if SESSION_KEY not in request.session or not get_user_session_key(request) == request.user.pk:
            # Setup session if not set
            login(request, request.user)
        return Response()

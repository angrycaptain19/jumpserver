from django.db.models import Q
from perms.models import ApplicationPermission
from applications.models import Application


def get_user_all_applicationpermissions_id(user):
    return ApplicationPermission.objects.valid().filter(
        Q(users=user) | Q(user_groups__users=user)
    ).distinct().values_list('id', flat=True)


def get_user_granted_all_applications(user):
    application_perms_id = get_user_all_applicationpermissions_id(user)
    return Application.objects.filter(
        granted_by_permissions__id__in=application_perms_id
    ).distinct()

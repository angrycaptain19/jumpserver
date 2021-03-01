# -*- coding: utf-8 -*-
#
from .. import utils
from users.models import User

from orgs.utils import current_org


class UserQuerysetMixin:
    def get_queryset(self):
        if self.request.query_params.get('all') or not current_org.is_real():
            return User.objects.exclude(role=User.ROLE.APP)
        else:
            return utils.get_current_org_members()

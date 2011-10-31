#coding: utf-8
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
import logging

@user_passes_test(lambda u: u.is_staff)
def login_as_user(request, user_id, can_su_staff=False):
    su_user = get_object_or_404(User, pk=user_id)
    staff_user = request.user
    logging.debug('User "%s" trying to log as "%s"' % (staff_user, su_user))
    if (su_user.is_staff or su_user.is_superuser) and not can_su_staff:
        logging.warn('Forbidden to "%s" to login as "%s"' % (staff_user, su_user))
        return HttpResponseForbidden("Cannot su other staff members")

    su_user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, su_user)
    logging.info('Staff member "%s" successfull logged as "%s"' % (staff_user, su_user))
    return HttpResponseRedirect("/")

#coding: utf-8
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login

@user_passes_test(lambda u: u.is_staff)
def login_as_user(request, user_id, can_su_staff=False):
    su_user = get_object_or_404(User, pk=user_id)
    if (su_user.is_staff or su_user.is_superuser) and not can_su_staff:
        return HttpResponseForbidden("Cannot su other staff members")

    su_user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, su_user)
    return HttpResponseRedirect("/")

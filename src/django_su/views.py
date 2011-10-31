#coding: utf-8
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login

@user_passes_test(lambda u: u.is_staff)
def login_as_user(request, user_id):
    su_user = get_object_or_404(User, pk=user_id)
    su_user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, su_user)
    return HttpResponseRedirect("/")

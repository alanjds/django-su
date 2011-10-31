from django.conf.urls.defaults import *

from django_su.views import login_as_user, su_exit

urlpatterns = patterns("",
    url(r"^(?P<user_id>[\d]+)/$", login_as_user, name="login_as_user"),
)
# -*- coding: utf-8 -*-

from django.urls import re_path
from .views import su_logout, su_login, login_as_user

urlpatterns = [
    re_path(r"^$", su_logout, name="su_logout"),
    re_path(r"^login/$", su_login, name="su_login"),
    re_path(r"^(?P<user_id>-?[\d]+)/$", login_as_user, name="login_as_user"),
]

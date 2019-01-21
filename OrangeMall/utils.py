# -*- coding: utf-8 -*-
from functools import wraps

from django.http import HttpResponseRedirect

__author__ = "chseng"
__date__ = "2019/1/21 19:01"

import hashlib

def create_fingerprint(url, type="md5"):
    """
    url指纹,默认为md5 16位;其他为sha1 32位
    :param url:
    :param type:
    :return:
    """
    minst = hashlib.md5() if type == "md5" else hashlib.sha1()
    minst.update(url.encode("utf8"))
    return minst.hexdigest()


def check_user_login(func):
   @wraps(func)
   def __wrapper(*args, **kwargs):
      #args = (request, )
      request = args[0]
      path = request.path
      if not request.session.has_key("muser"):
         return HttpResponseRedirect(f"/user/login/?next={path}")
      return func(*args, **kwargs)
   return __wrapper

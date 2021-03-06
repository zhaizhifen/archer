# coding = utf-8
from django.http import HttpResponseRedirect

class CheckLoginMiddleware(object):
    def process_request(self, request):
        """
        本系统没有采用django.contrib.auth组件，自己简单实现了一把认证系统。
        该函数在每个函数之前检查是否登录，若未登录，则重定向到/login/
        """
        if request.session.get('login_username', False) in (False, '匿名用户'):
            if request.path not in ('/login/', '/authenticate/'):
                return HttpResponseRedirect('/login/')

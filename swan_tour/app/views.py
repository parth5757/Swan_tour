from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
class BaseView(LoginRequiredMixin):
    '''Base View is here'''
    login_url = '/login/'

class SuperUserView(LoginRequiredMixin):
    '''Super user is not check'''
    def test_func(self):
        return self.request.user.is_superuser
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

    login_url = '/login/'

class ErrorView(View):
    def get(self, request, undefined_route):
        return render(request, 'error.html')
    
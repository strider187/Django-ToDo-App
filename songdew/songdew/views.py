from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'index.html'

class LoginSuccess(TemplateView):
    template_name = 'login_success.html'

class LogoutSuccess(TemplateView):
    template_name = 'logout_success.html'

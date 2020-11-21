from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'


class LogInRedirectPage(TemplateView):
    template_name = 'login_redirect.html'


class LogOutRedirectPage(TemplateView):
    template_name = 'logout_redirect.html'
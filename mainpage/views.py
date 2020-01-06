from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View
from .models import Hero
from .models import Services
from .models import Why
from .models import Work


class HeroView(View):
    def get(self, request):
        hero_section = Hero.objects.all()
        services_section = Services.objects.all()
        why_section = Why.objects.all()
        work_section = Work.objects.all()
        return render(request, "pages/mainpage_list.html",
                      {
                          "hero_list": hero_section,
                          "services_list": services_section,
                          "why_list": why_section,
                          "work_list": work_section,
                      })


def admin_list(request):
    return render(request, "pages/admin_app.html")


# РЕГИСТРАЦИЯ
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "pages/register_page.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "pages/login_page.html"
    success_url = "/adminapp/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

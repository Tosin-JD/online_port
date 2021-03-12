from django.shortcuts import render
from .models import Employee

# import model DockManifest
from ship.models import DockManifest

from django.views import generic
from accounts.models import MyUser
from accounts.forms import UserCreationForm

# Create your views here.
class SignUp(generic.CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = "accounts/sign_up.html"
    success_url = "accounts/login"


class ProfilePage(generic.TemplateView):
    model = DockManifest
    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        context['dock_manifest'] = reversed(DockManifest.objects.\
                                    all().order_by('-timestamp'))
        return context


class ThanksPage(generic.TemplateView):
    template_name = "accounts/thanks.html"


class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'accounts/employee_list.html'

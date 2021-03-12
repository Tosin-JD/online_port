from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from .models import (Dock, DockManifest,
                     CargoHazard, DockSupervisor,
                     Person, Ship, State)
from .forms import DockManifestForm
from services.models import Service, AnimatedIntro, WelcomeNote




# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['intro_list'] = AnimatedIntro.objects.all()
        context['welcomenotes'] = WelcomeNote.objects.all()[:3]
        return context


def dock_overview(request):
    """A view to display an overview of docks"""
    template = 'ship/dock_overview.html'
    context = {
        'data': []
    }

    docks = Dock.objects.all()
    for dock in docks:
        hazards = CargoHazard.objects.filter(container__ship__dock=dock).distinct()
        context['data'].append({
            'dock': dock,
            'hazards': hazards
        })

    return render(request, template, context)


class DockDetail(LoginRequiredMixin, generic.DetailView):
    model = Dock
    template_name = 'ship/dock_details.html'


@login_required
def user_profile(request):
    """A view to display the details of a logged in user."""
    template = 'ship/user_profile.html'
    person = get_object_or_404(Person, user=request.user)
    ships = Ship.objects.filter(captain__person=person)

    context = {
        'person': person,
        'ships': ships,
    }

    return render(request, template, context)



class CreateDockManifest(LoginRequiredMixin, generic.CreateView):
    model = DockManifest
    form_class = DockManifestForm
    template_name = 'ship/manifest_form.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        all_manifest = DockManifest.objects.all()
        if (not all_manifest):
            form.instance.current_position = State.due_to_offload
        else:
            first = all_manifest.first()
            last = all_manifest.last()
            if last.is_due_offload():
                form.instance.current_position = State.not_offloaded
            elif first.is_offloaded():
                form.instance.current_position = State.due_to_offload
            elif last.is_not_offloaded():
                form.instance.current_position = State.not_offloaded
        return super(CreateDockManifest, self).form_valid(form)


class DockManifestList(generic.ListView):
    model = DockManifest
    template_name = 'ship/manifest_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DockManifestList, self).get_context_data(*args, **kwargs)
        context['offloaded'] = DockManifest.objects.filter\
                                    (current_position__iexact = 'oo')
        context['due_to_offload'] = DockManifest.objects.filter\
                                    (current_position__iexact = 'dd')
        context['not_offloaded'] = DockManifest.objects.filter\
                                    (current_position__iexact = 'yy')
        return context


class DockManifestDetail(generic.DetailView):
    model = DockManifest
    template_name = 'ship/manifest_detail.html'


class DockManifestUpdate(generic.UpdateView):
    model = DockManifest
    template_name = 'ship/manifest_form.html'


class DockManifestDelete(generic.DeleteView):
    model = DockManifest
    template_name = 'ship/manifest_delete.html'


class ShipList(generic.ListView):
    model = Ship
    template_name = 'ship/ship_list.html'


@login_required
def offload(requst, pk):
    """offload each dock manifest using queue """

    # get the item to offload
    dock_manifest = get_object_or_404(DockManifest, pk=pk)

    #if (dock_manifest.current_position == 'dd' or check_next):
    if (dock_manifest.is_due_offload()):
        dock_manifest.current_position = State.offloaded

        try:
            dock_manifest_next = dock_manifest.\
                                            get_next_by_timestamp()
        except ObjectDoesNotExist:
            print("No Previous Item")
        else:
            dock_manifest_next.current_position = State.due_to_offload
            dock_manifest_next.save()

        dock_manifest.save()

    return redirect(reverse_lazy('accounts:profile'))


def print_manifest(request, pk):
    pass

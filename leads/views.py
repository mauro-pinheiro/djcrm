from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import *
from .models import Lead, Agent
from .forms import LeadModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadUpdateView(UpdateView):
    template_name = "leads/update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name = "leads/delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(requestm, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')

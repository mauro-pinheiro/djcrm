from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import *
from .models import Lead, Agent
from .forms import LeadModelForm, UserCreationForm

class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("leads:lead-list")

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
    
    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site so see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

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

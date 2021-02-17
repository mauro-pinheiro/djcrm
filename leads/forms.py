from django import forms
from django.contrib.auth import forms as authForms, get_user_model
from .models import Lead

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class UserCreationForm(authForms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': authForms.UsernameField}
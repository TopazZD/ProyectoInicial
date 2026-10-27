from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from .comunas import obtener_comunas


class RegistroForm(UserCreationForm):
    comuna = forms.ChoiceField(
        choices=[('', 'Selecciona tu comuna')] + [(c, c) for c in obtener_comunas()]
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'comuna']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Perfil.objects.create(usuario=user, comuna=self.cleaned_data['comuna'])
        return user
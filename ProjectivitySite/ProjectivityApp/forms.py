from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from ProjectivityApp.models import Utilizator


def verificare_combinatie_utilizator_parola(cod_utilizator, parola):
    try:
        utilizator = Utilizator.objects.get(cod_utilizator=cod_utilizator)
        if utilizator.parola == parola:
            return True
    except Utilizator.DoesNotExist:
        pass

    return False

class LoginForm(forms.Form):
    cod_utilizator = forms.CharField(label='Utilizator', max_length=100)
    parola = forms.CharField(label='Parola', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        cod_utilizator = cleaned_data.get('cod_utilizator')
        parola = cleaned_data.get('parola')

        if cod_utilizator and parola:
            if not verificare_combinatie_utilizator_parola(cod_utilizator, parola):
                raise forms.ValidationError('Nume de utilizator sau parolă greșite')

class HomeForm(forms.Form):
    nume = forms.CharField(
        label="Nume",
        max_length=255,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    
class ProjectForm(forms.Form):
    nume_proiect = forms.CharField(max_length=100)
    status_proiect = forms.ChoiceField(choices=[('red', 'Anulat'), ('yellow', 'In lucru'), ('green', 'Terminat')])
    descriere = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 250}))
    deadline_data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    deadline_ora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
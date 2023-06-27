from django import forms
from django.utils import timezone
# from django.contrib.auth.forms import AuthenticationForm
from ProjectivityApp.models import Utilizator, Proiect, Task, Sedinta


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
    
class ProiectForm(forms.ModelForm):
    class Meta:
        model = Proiect
        fields = ['nume_proiect', 'status', 'descriere', 'data_inceput', 'data_sfarsit']

    def save(self, cod_departament):
        proiect = super().save(commit=False)
        proiect.cod_departament = cod_departament
        proiect.data_inceput = timezone.now()

        if proiect.status_proiect == 'green':
            proiect.data_sfarsit = timezone.now()

        proiect.save()
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nume_task', 'status', 'descriere', 'data']

    def save(self, cod_departament):
        task = super().save(commit=False)
        task.cod_departament = cod_departament
        task.data_inceput = timezone.now()

        if task.status_task == 'green':
            task.data_sfarsit = timezone.now()

        task.save()
        
class SedintaForm(forms.ModelForm):
    class Meta:
        model = Sedinta
        fields = ['nume_sedinta', 'descriere', 'data_sedinta', 'ora_inceput', 'ora_sfarsit']

    def save(self, cod_departament):
        sedinta = super().save(commit=False)
        sedinta.cod_departament = cod_departament
        sedinta.data_inceput = timezone.now()

        sedinta.save()

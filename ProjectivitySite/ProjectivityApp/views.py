
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from getpass import getpass
from django.core.exceptions import PermissionDenied
from .models import Proiect
from .forms import LoginForm, HomeForm, ProjectForm

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cod_utilizator = form.cleaned_data['cod_utilizator']
            parola = form.cleaned_data['parola']

            if len(cod_utilizator) < 3:
                mesaj_eroare = "Numele de utilizator trebuie să aibă cel puțin 3 caractere."
                return render(request, 'login.html', {'form': form, 'mesaj_eroare': mesaj_eroare})
            if len(parola) < 3:
                mesaj_eroare = "Parola trebuie să aibă cel puțin 3 caractere."
                return render(request, 'login.html', {'form': form, 'mesaj_eroare': mesaj_eroare})

            user = authenticate(request, cod_utilizator=cod_utilizator, parola=parola)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                mesaj_eroare = "Nume de utilizator sau parolă greșite"
                return render(request, 'login.html', {'form': form, 'mesaj_eroare': mesaj_eroare})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def HomeView(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data['nume']
            return render(request, 'home.html', {'form': form, 'nume': nume})
    else:
        form = HomeForm()

    return render(request, 'home.html', {'form': form})

@login_required
def ProiectView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data_inceput = timezone.now()  
            data_sfarsit = None

            if form.cleaned_data['status_proiect'] == 'green':
                data_sfarsit = timezone.now()

            proiect = Proiect(
                numire_proiect=form.cleaned_data['denumire_proiect'],
                status_proiect=form.cleaned_data['status_proiect'],
                descriere=form.cleaned_data['descriere'],
                data_inceput=data_inceput,
                data_sfarsit=data_sfarsit,
                status='green',
                cod_departament=request.user.cod_departament
            )
            proiect.save()
            return redirect('proiecte')
    else:
        form = ProjectForm()

    if request.user.is_authenticated:
        proiecte = Proiect.objects.filter(cod_departament=request.user.cod_departament)
    else:
        proiecte = None
        
    context = {
        'form': form,
        'proiecte': proiecte
    }
    return render(request, 'proiecte.html', context)

# @login_required
# def modifica_utilizator(request, cod_utilizator):
#     prompt_cod_acces()
#     utilizator = Utilizator.objects.get(cod_utilizator=cod_utilizator)
#     if request.method == 'POST':
#         if request.user.is_superuser and request.user.is_staff:
#             utilizator.cod_utilizator = request.POST.get('cod_utilizator')
#             utilizator.parola = request.POST.get('parola')
#             utilizator.cod_departament = request.POST.get('cod_departament')
#             utilizator.cod_echipa = request.POST.get('cod_echipa')
#             utilizator.notificari = request.POST.get('notificari')
#         else:
#             utilizator.adresa_email = request.POST.get('adresa_email')
#             utilizator.nr_telefon = request.POST.get('nr_telefon')
#             utilizator.cod_echipa = request.POST.get('cod_echipa')
#             utilizator.locatie_birou = request.POST.get('locatie_birou')
#             utilizator.atributii = request.POST.get('atributii')
#             utilizator.notificari = request.POST.get('notificari')
        
#         utilizator.save()
#         return render(request, 'detalii_utilizator.html', {'mesaj': 'Utilizator modificat cu succes!'})
#     else:
#         if request.user.is_superuser and request.user.is_staff:
#             return render(request, 'modifica_utilizator_admin.html', {'utilizator': utilizator})
#         else:
#             return render(request, 'modifica_utilizator.html', {'utilizator': utilizator})

@login_required
def Detalii_utilizatorView(request):
    if request.user.is_authenticated:
        utilizator = request.user
        context = {'utilizator': utilizator}
        return render(request, 'detalii_utilizator.html', context)
    else:
        return redirect('login')
    
# @login_required
# def Detalii_utilizatorView(request):
#     utilizator = request.user

#     context = {
#         'utilizator': utilizator
#     }

#     return render(request, 'detalii_utilizator.html', context)

def Contact2View(request):
    return render(request, 'contact2.html')

def Info_utileView(request):
    return render(request, 'info_utile.html')

@login_required
def ContactView(request):
    return render(request, 'contact.html')

# @login_required
# def afiseaza_utilizator(request):
#     utilizator = Utilizator.objects.all()
#     return render(request, 'detalii_utilizator.html', {'utilizator': utilizator})
 
def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('login')


# # def detalii_utilizator(request, cod_utilizator):
# #     utilizator = Utilizator.objects.get(pk=cod_utilizator)
# #     return render(request, 'detalii_utilizator.html', {'utilizator': utilizator})

# @login_required
# def departament(request):
#     departament = Departament.objects.all()
#     return render(request, 'detalii_utilizator.html', {'departament': departament})

# @login_required
# def proiect(request):
#     proiecte = Proiect.objects.all()
#     return render(request, 'proiecte.html', {'proiecte': proiecte})

# @login_required
# def task(request):  
#     task = Task.objects.all()
#     return render(request, 'taskuri.html', {'task': task})

# @login_required
# def sedinta(request):
#     sedinta = Sedinta.objects.all()
#     return render(request, 'sedinte.html', {'sedinta': sedinta})

# @login_required
# def chat(request):
#     chat = Chat.objects.all()
#     return render(request, 'chat.html', {'chat': chat})

# @login_required
# def mesaj(request):
#     mesaj = Mesaj.objects.all()
#     return render(request, 'chat.html', {'mesaj': mesaj})

# @login_required
# def forum(request):
#     forum = Forum.objects.all()
#     return render(request, 'forum.html', {'forum': forum})

# @login_required
# def postare(request, cod_postare):
#     postare = Postare.objects.get(pk=cod_postare)
#     return render(request, 'chat.html', {'postare': postare})

# @login_required
# def comentariu(request, cod_postare):
#     comentariu = Comentariu.objects.get(pk=cod_postare)
#     return render(request, 'chat.html', {'comentariu': comentariu})



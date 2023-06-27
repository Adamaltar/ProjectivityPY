from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# from getpass import getpass
# from django.core.exceptions import PermissionDenied
from .models import Proiect, Mesaj, Chat, Task, Sedinta, Utilizator, Departament, Echipe, Forum, Postare, Comentariu
from .forms import LoginForm, ProiectForm, TaskForm, SedintaForm

def init(request, current_user_id):
    if request.user.is_authenticated:
        current_user_id = request.user.cod_utilizator
    else:
        current_user_id = None

def get_all_records():
    records = Utilizator.objects.all()
    return records

def get_filtered_records():
    records = Utilizator.objects.filter(col1='cod_utilizator', col2='cod_departament')
    return records

# def get_aggregated_result():
#     result = Utilizator.objects.aggregate(count=Count('col1'))
#     return result


def get_all_records():
    records = Departament.objects.all()
    return records


def get_all_records():
    records = Chat.objects.all()
    return records

def get_filtered_records():
    records = Chat.objects.filter(col1='cod_utilizator', col2='cod_chat', col3='cod_mesaj')
    return records

# def get_aggregated_result():
#     result = Chat.objects.aggregate(count=Count('col1'))
#     return result

def get_all_records():
    records = Proiect.objects.all()
    return records

def get_filtered_records():
    records = Proiect.objects.filter(col1='cod_utilizator', col2='cod_chat', col3='cod_mesaj')
    return records

# def get_aggregated_result():
#     result = Proiect.objects.aggregate(count=Count('col1'))
#     return result

def get_all_records():
    records = Task.objects.all()
    return records

def get_filtered_records():
    records = Task.objects.filter(col1='cod_utilizator', col2='cod_chat', col3='cod_mesaj')
    return records

# def get_aggregated_result():
#     result = Task.objects.aggregate(count=Count('col1'))
#     return result

def get_all_records():
    records = Sedinta.objects.all()
    return records

def get_filtered_records():
    records = Sedinta.objects.filter(col1='cod_utilizator', col2='cod_chat', col3='cod_mesaj')
    return records

# def get_aggregated_result():
#     result = Sedinta.objects.aggregate(count=Count('col1'))
#     return result

def get_all_records():
    records = Mesaj.objects.all()
    return records

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cod_utilizator = form.cleaned_data['cod_utilizator']
            parola = form.cleaned_data['parola']

            if len(cod_utilizator) < 3:
                mesaj_eroare = "Numele de utilizator trebuie să aibă cel puțin 3 caractere."
                messages.error(request, mesaj_eroare)
                return render(request, 'login.html', {'form': form})

            if len(parola) < 3:
                mesaj_eroare = "Parola trebuie să aibă cel puțin 3 caractere."
                messages.error(request, mesaj_eroare)
                return render(request, 'login.html', {'form': form})

            user = authenticate(request, cod_utilizator=cod_utilizator, parola=parola)
            if user is not None:
                login(request, user)
                current_user_id = user.cod_utilizator
                init(request, current_user_id)
                return redirect('home')
            else:
                mesaj_eroare = "Nume de utilizator sau parolă greșite"
                messages.error(request, mesaj_eroare)
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def HomeView(request):
    return render(request, 'home.html')

@login_required
def get_users(request):
    users = Utilizator.objects.values('cod_utilizator')
    data = list(users)
    return JsonResponse(data, safe=False)

@login_required
def ProiectView(request):
    if request.method == 'POST':
        form = ProiectForm(request.POST)
        if form.is_valid():
            form.save(request.user.cod_departament)
            return redirect('proiecte')
    else:
        form = ProiectForm()

    if request.user.is_authenticated:
        proiecte = Proiect.objects.filter(cod_departament=request.user.cod_departament)
    else:
        proiecte = None

    context = {
        'form': form,
        'proiecte': proiecte
    }
    return render(request, 'proiecte.html', context)

@login_required
def TaskView(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(request.user.cod_departament)
            return redirect('taskuri')
    else:
        form = TaskForm()

    if request.user.is_authenticated:
        taskuri = Task.objects.filter(cod_departament=request.user.cod_departament)
    else:
        taskuri = None

    context = {
        'form': form,
        'taskuri': taskuri
    }
    return render(request, 'taskuri.html', context)

@login_required
def SedintaView(request):
    if request.method == 'POST':
        form = SedintaForm(request.POST)
        if form.is_valid():
            form.save(request.user.cod_departament)
            return redirect('sedinte')
    else:
        form = SedintaForm()

    if request.user.is_authenticated:
        sedinte = Sedinta.objects.filter(cod_departament=request.user.cod_departament)
    else:
        sedinte = None

    context = {
        'form': form,
        'sedinte': sedinte
    }
    return render(request, 'sedinte.html', context)

@csrf_exempt  
@login_required
def salveaza_proiect(request):
    if request.method == 'POST':
        data = request.POST
        data_inceput = timezone.now()
        data_sfarsit = None

        if data['status_proiect'] == 'green':
            data_sfarsit = timezone.now()

        proiect = Proiect(
            nume_proiect=data['nume_proiect'],
            status_proiect=data['status_proiect'],
            descriere=data['descriere'],
            data_inceput=data_inceput,
            data_sfarsit=data_sfarsit,
            status='green',
            cod_departament=request.user.cod_departament
        )
        proiect.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@login_required
def Detalii_utilizatorView(request):
    if request.user.is_authenticated:
        utilizator = request.user
        context = {'utilizator': utilizator}
        return render(request, 'detalii_utilizator.html', context)
    else:
        return redirect('login')
    
from django.http import JsonResponse

def get_notifications(request):

    if request.user.is_authenticated:
        cod_utilizator = request.user.cod_utilizator

        notifications = [
            'Un nou proiect a fost adăugat pentru departamentul ' + request.user.cod_departament,
            'Ați fost adăugat într-un nou chat'
        ]

        # proiecte_notificari = get_notificari_proiecte(request.user.cod_departament)
        # notifications.extend(proiecte_notificari)

        # taskuri_notificari = get_notificari_taskuri(request.user.cod_departament)
        # notifications.extend(taskuri_notificari)
        
        # taskuri_notificari = get_notificari_sedinte(request.user.cod_departament)
        # notifications.extend(taskuri_notificari)

        # chaturi_notificari = get_notificari_chaturi(request.user.cod_utilizator)
        # notifications.extend(chaturi_notificari)

        return JsonResponse({'notifications': notifications})
    else:
        return JsonResponse({'notifications': []})

def Contact2View(request):
    return render(request, 'contact2.html')

def Info_utileView(request):
    return render(request, 'info_utile.html')

@login_required
def ContactView(request):
    return render(request, 'contact.html')
 
def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('login')


@login_required
def get_users(request):
    users = Utilizator.objects.all()
    data = [{'cod_utilizator': user.cod_utilizator} for user in users]
    return JsonResponse(data, safe=False)

@login_required
def add_chat_member(request, cod_chat, cod_utilizator):
    chat = get_object_or_404(Chat, id=cod_chat)
    user = get_object_or_404(Utilizator, id=cod_utilizator)

    if user in chat.cod_utilizator.all():
        return JsonResponse({'success': False, 'message': 'Utilizatorul este deja membru al chat-ului.'})
    
    if chat.cod_utilizator.count() >= 10:
        return JsonResponse({'success': False, 'message': 'Chat-ul are deja 10 membri.'})
    
    chat.cod_utilizator.add(user)
    chat.save()
    
    return JsonResponse({'success': True, 'message': 'Utilizatorul a fost adăugat ca membru al chat-ului.'})
 
@login_required
def update_chat_in_database(request, cod_chat):
    if request.method == 'POST':
        nume_chat = request.POST.get('nume_chat')
        continut = request.POST.get('continut')
        chat = get_object_or_404(Chat, id=cod_chat)
        chat.nume_chat = nume_chat
        chat.continut = continut
        chat.save()
        print('Chat-ul a fost actualizat în baza de date.')
        return HttpResponse('Chat-ul a fost actualizat în baza de date.')

@login_required
def delete_chat_from_database(request, cod_chat):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=cod_chat)
        chat.delete()
        print('Chat-ul a fost șters din baza de date.')
        return HttpResponse('Chat-ul a fost șters din baza de date.')

@login_required
def save_chat_to_database(request):
    if request.method == 'POST':
        cod_utilizator = request.POST.get('cod_utilizator')
        membrii = request.POST.getlist('membrii')
        nume_chat = request.POST.get('nume_chat')
        continut = request.POST.get('continut')
        chat = Chat(cod_utilizator=cod_utilizator, nume_chat=nume_chat, continut=continut)
        chat.save()
        chat.membrii.set(membrii)
        print('Chat-ul a fost salvat în baza de date.')
        return HttpResponse('Chat-ul a fost salvat în baza de date.')

@login_required
def invite_members_to_chat(request, cod_chat):
    if request.method == 'POST':
        user = request.POST.get('user')
        chat = get_object_or_404(Chat, id=cod_chat)

        if chat.cod_utilizator.count() >= 10:
            return JsonResponse({'success': False, 'message': 'Numărul maxim de membri a fost atins.'})

        if not Utilizator.objects.filter(cod_utilizator=user).exists():
            return JsonResponse({'success': False, 'message': 'Utilizatorul specificat nu există.'})

        chat.cod_utilizator.add(Utilizator.objects.get(cod_utilizator=user))
        print('Utilizatorul', user, 'a fost adăugat în chat-ul din baza de date.')
        return JsonResponse({'success': True, 'message': 'Utilizatorul a fost adăugat în chat.'})

@login_required
def save_message_to_database(request, cod_chat):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=cod_chat)
        mesaj = request.POST.get('mesaj')
        message = Mesaj(chat=chat, mesaj=mesaj)
        message.save()
        print('Mesajul a fost salvat în baza de date.')
        return HttpResponse('Mesajul a fost salvat în baza de date.')

def rapoarte(request):
    proiecte = Proiect.objects.all()
    context = {
        'proiecte': proiecte
    }
    taskuri = Task.objects.all()
    context = {
        'taskuri': taskuri
    }
    sedinte = Sedinta.objects.all()
    context = {
        'sedinte': sedinte
    }
    return render(request, 'rapoarte.html', context)



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

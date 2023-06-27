# import os
# from django.conf import settings

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProjectivitySite.settings")
# settings.configure()

# import django
# django.setup()

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class UtilizatorManager(BaseUserManager):
    
    def create_superuser(self, cod_utilizator, parola=None, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser trebuie sa fie atribuit is_staff=True.'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser trebuie sa fie atribuit is_superuser=True.'))
        
        return self.create_user(cod_utilizator, parola, **other_fields)    
    
    def create_user(self, cod_utilizator, parola=None, **other_fields):
        if not cod_utilizator:
            raise ValueError(_('Codul utilizatorului trebuie specificat'))

        user = self.model(cod_utilizator=cod_utilizator, **other_fields)
        user.set_password(parola)
        user.save(using=self._db)
        return user


class Departament(models.Model):
    cod_departament = models.AutoField(primary_key=True)
    nume_departament = models.CharField(max_length=50)


class Echipe(models.Model):
    cod_echipa = models.AutoField(primary_key=True)    
    nume_echipa = models.CharField(max_length=50)
    cod_departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default='')

class Utilizator(AbstractBaseUser, PermissionsMixin):
    cod_utilizator = models.TextField(max_length=50, unique=True, default='')
    nume = models.TextField(max_length=50, blank=True)
    prenume = models.TextField(max_length=50, blank=True)
    cod_departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default='')
    cod_echipa = models.ForeignKey(Echipe, on_delete=models.CASCADE, default='')
    parola = models.TextField(max_length=50, blank=True)
    adresa_email = models.EmailField(_('adresa email'), unique=True)
    nr_telefon = models.CharField(max_length=15)
    locatie_birou = models.CharField(max_length=50, blank=True)
    atributii = models.CharField(max_length=100, blank=True)
    notificari = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    objects = UtilizatorManager()

    USERNAME_FIELD = 'cod_utilizator'
    # REQUIRED_FIELDS = ['nume', 'prenume']

    # class Meta:
    #     app_label = 'ProjectivityApp'

    def __str__(self):
        return str(self.cod_utilizator)

# def nume_complet(self):
#     return f"{self.nume} {self.prenume}"


class Proiect(models.Model):
    cod_proiect = models.AutoField(primary_key=True)
    nume_proiect = models.CharField(max_length=20)
    descriere = models.CharField(max_length=50)
    data_inceput = models.DateField()
    data_sfarsit = models.DateField()
    status = models.CharField(max_length=15)
    cod_departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default='')


class Task(models.Model):
    cod_task = models.AutoField(primary_key=True)
    nume_task = models.CharField(max_length=20)
    descriere = models.CharField(max_length=50)
    data = models.DateField()
    status = models.CharField(max_length=15)
    cod_departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default='')
    cod_echipa = models.ForeignKey(Echipe, on_delete=models.CASCADE, default='')


class Sedinta(models.Model):
    cod_sedinta = models.AutoField(primary_key=True)
    nume_sedinta = models.CharField(max_length=20)
    descriere = models.CharField(max_length=50)
    data_sedinta = models.DateField()
    ora_inceput = models.TimeField()
    ora_sfarsit = models.TimeField()
    cod_departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default='')


class Chat(models.Model):
    cod_chat = models.AutoField(primary_key=True)   
    cod_utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE, max_length=50, default='')
    nume_chat = models.CharField(max_length=200)
    continut = models.TextField()
    
    def __str__(self):
        return self.nume_chat    


class Mesaj(models.Model):
    cod_mesaj = models.AutoField(primary_key=True)
    mesaj = models.CharField(max_length=100)
    data_mesaj = models.DateTimeField()
    cod_utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE, max_length=50, default='')
    cod_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.mesaj    

class Forum(models.Model):
    cod_forum = models.AutoField(primary_key=True)
    cod_utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE, max_length=50, default='')
    nume_forum = models.CharField(max_length=50)
    descriere = models.TextField()


class Postare(models.Model):
    cod_postare = models.AutoField(primary_key=True)
    titlu = models.CharField(max_length=100)
    continut = models.TextField()
    data_postarii = models.DateField()
    cod_utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE, max_length=50, default='')
    cod_forum = models.ForeignKey(Forum, on_delete=models.CASCADE, default='')


class Comentariu(models.Model):
    cod_comentariu = models.AutoField(primary_key=True)
    continut = models.TextField()
    data_comentariului = models.DateField()
    cod_utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE, max_length=50, default='')
    cod_postare = models.ForeignKey(Postare, on_delete=models.CASCADE, default='')


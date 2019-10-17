from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mois(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='img', blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mois"
        verbose_name_plural = "Mois"

    def __str__(self):
        return self.titre

class Module(models.Model):
    mois = models.ForeignKey('Mois', on_delete = models.CASCADE, related_name='mois_module')
    langage = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='img', blank=True)
    prix = models.IntegerField()

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.langage

class Chapitre(models.Model):
    module = models.ForeignKey('Module', on_delete = models.CASCADE, related_name='module_chapitre')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='img', blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chapitre"
        verbose_name_plural = "Chapitres"

    def __str__(self):
        return self.titre

class Cours(models.Model):
    chapitre = models.ForeignKey('Chapitre', on_delete = models.CASCADE, related_name='chapitre_cours')
    titre = models.CharField(max_length=255)
    video = models.FileField()
    image = models.ImageField(upload_to='img', blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.titre

class User_cours(models.Model):
    module = models.ForeignKey('Module', on_delete = models.CASCADE, related_name='module_user')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='cour_user')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user

#python3 manage.py admin_generator Api >> Api/admin.py
#python manage.py seed Api --number=15

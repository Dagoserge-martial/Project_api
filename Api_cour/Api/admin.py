from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MoisAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class ModuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'mois',
        'langage',
        'description',
        'image',
        'prix',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'mois',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'mois',
        'langage',
        'description',
        'image',
        'prix',
        'statut',
        'date_add',
        'date_upd',
    )


class ChapitreAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'module',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'module',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'module',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class CoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'chapitre',
        'titre',
        'video',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'chapitre',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'chapitre',
        'titre',
        'video',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class User_coursAdmin(admin.ModelAdmin):

    list_display = ('id', 'module', 'user', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'module',
        'user',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'module',
        'user',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Mois, MoisAdmin)
_register(models.Module, ModuleAdmin)
_register(models.Chapitre, ChapitreAdmin)
_register(models.Cours, CoursAdmin)
_register(models.User_cours, User_coursAdmin)

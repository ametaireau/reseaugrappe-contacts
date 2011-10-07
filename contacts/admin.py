# -*- coding: utf-8 -*-
from django.contrib import admin
from reseaugrappe.contacts.models import *

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        ("", {
            'fields': [('surname', 'name'), 
                       ('phone', 'cellphone'), 
                       'email']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at']
        }),
    )
    list_display = ['surname', 'name', 'email', 'cellphone', 'phone']
    list_editable = ['email', 'cellphone', 'phone']


class StructureAdmin(ContactAdmin):

    fieldsets = (
        ("", {
            'fields': ['structure_name',
                       ('surname', 'name'), 
                       ('phone', 'cellphone'), 
                       'email']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at',
                'contact_grappe']
        }),
    )
    list_display = ['structure_name', ] + ContactAdmin.list_display


class AnimationAdmin(ContactAdmin):

    fieldsets = (
        ("", {
            'fields': [('title', 'cost'),
                       ('surname', 'name'), 
                       ('phone', 'cellphone'), 
                       'email']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at',
                'contact_grappe']
        }),
    )
    list_display = ['title'] + ContactAdmin.list_display + ['cost']

admin.site.register((Radio, Tv, Website, Press, Administration, 
                     Entreprise, Association), StructureAdmin)
admin.site.register((Conf, Film, AnimPedago, Musique, Exposition), AnimationAdmin)
admin.site.register(ContactGrappe, ContactAdmin)

from django.contrib import admin
from .models import *



admin.site.register(Fournisseur)
admin.site.register(Commande)
#admin.site.register(Operation)
admin.site.register(Facture)
admin.site.register(Departement)
admin.site.register(Mouvement)
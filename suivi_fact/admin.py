from django.contrib import admin
from .models import *


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('fourn_id', 'nom', 'ville')
    
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('comm_id', )
    
class FactureAdmin(admin.ModelAdmin):
    list_display = ('fact_id', 'montant', 'tauxTVA', 'montantTTC', 'Date_arrivee', 'Date_mandat', 'Date_compta', 'num_op', 'num_fact')
    
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Commande, CommandeAdmin)
#admin.site.register(Operation)
admin.site.register(Facture, FactureAdmin)
admin.site.register(Departement)
admin.site.register(Mouvement)

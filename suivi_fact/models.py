from tkinter import CASCADE
from django.db import models

# Create your models here.

class Fournisseur(models.Model):
    fourn_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=20)

class Commandes(models.Model):
    comm_id = models.AutoField(primary_key=True)
    #date = 
    num_fourn = models.ForeignKey(Fournisseur, on_delete=CASCADE)

class Factures(models.Model):
    fact_id = models.AutoField(primary_key=True)
    num_comm = models.ForeignKey(Commandes, on_delete=CASCADE)
    montant= models.FloatField()
    tauxTVA = models.FloatField()
    montantTTC = models.FloatField()
    Date_mandat = models.DateTimeField(default=timezone.now)
    

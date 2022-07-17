from django.db import models
from django.utils import timezone

# Create your models here.

class Fournisseur(models.Model):
    fourn_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=20)

class Commandes(models.Model):
    comm_id = models.AutoField(primary_key=True)
    #date = 
    num_fourn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Factures(models.Model):
    fact_id = models.AutoField(primary_key=True)
    num_comm = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    montant= models.FloatField()
    tauxTVA = models.FloatField()
    montantTTC = models.FloatField()
    Date_arrivee = models.DateTimeField(default=timezone.now)
    Date_mandat = models.DateTimeField()
    Date_compta = models.DateTimeField()
    num_oper = models.IntegerField()

class Departements(models.Model):
    depart_id = models.AutoField(primary_key=True)
    nom_depart = models.CharField(max_length=20)


class Mouvements(models.Model):
    mouv_id = models.AutoField(primary_key=True)
    num_fact = models.ForeignKey(Factures, on_delete=models.CASCADE)
    deplacement = models.ForeignKey(Departements, on_delete=models.DO_NOTHING)
    time_mouv = models.DateTimeField(default=timezone.now)
    motif = models.CharField(max_length=1500)


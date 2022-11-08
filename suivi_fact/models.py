from django.db import models
from django.utils import timezone

# Create your models here.

class Fournisseur(models.Model):
    fourn_id = models.AutoField(primary_key=True, verbose_name='fourn_id')
    nom = models.CharField(max_length=50, verbose_name='nom')
    ville = models.CharField(max_length=20, verbose_name='ville')
    def __str__(self):
        return "{}- {} {}".format(self.fourn_id, self.nom,self.ville)

class Commande(models.Model):
    comm_id = models.AutoField(primary_key=True, verbose_name='comm_id')
    num_fourn = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.comm_id, self.num_fourn)

# class Operation(models.Model):
#     num_oper = models.AutoField(primary_key=True, blank=True) #, null=True
#     label = models.CharField(max_length=50, blank=True, null=True)
#     def __str__(self):
#         return "{}: {}".format(self.num_oper, self.label)

class Facture(models.Model):
    fact_id = models.AutoField(primary_key=True, verbose_name='fact_id')
    num_comm = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant= models.FloatField(verbose_name='montant')
    tauxTVA = models.FloatField(verbose_name='tauxTVA')
    montantTTC = models.FloatField(verbose_name='montantTTC')
    Date_arrivee = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date_arrivee')
    Date_mandat = models.DateTimeField(null=True, blank=True, verbose_name='Date_mandat')
    Date_compta = models.DateTimeField(null=True, blank=True, verbose_name='Date_compta')
    num_op = models.IntegerField(blank=True, null=True, verbose_name='num_op')
    num_fact = models.CharField(max_length=500, null=True, blank=True, verbose_name='num_fact')
    def __str__(self):
        return "{}".format(self.fact_id)

class Departement(models.Model):
    depart_id = models.AutoField(primary_key=True)
    nom_depart = models.CharField(
        max_length=3,
        choices=[
            ('BO',"Bureau d'ordre"),
            ('DCF',"Département de comptabilité et de finance"),
            ('ST',"Service technique"),
        ])
    def __str__(self):
        return "{} {}".format(self.depart_id,self.nom_depart)

class Mouvement(models.Model):
    mouv_id = models.AutoField(primary_key=True)
    num_fact = models.ForeignKey(Facture, on_delete=models.CASCADE)
    deplacement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    time_mouv = models.DateTimeField(auto_now_add=True, editable=False)
    motif = models.CharField(max_length=1500)
    def __str__(self):
        return "{} {}".format(self.mouv_id,self.motif)
        
        
#tzid field dyal num_op : packages
#ta3wti les permission dyal l users dyalk
#

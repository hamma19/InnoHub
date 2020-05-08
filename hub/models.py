from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

def endsswith(ch):
    if not str(ch).endswith("@esprit.tn"):
        raise ValidationError("Votre Email doit etre @esprit.tn",params={'value':ch})
# Create your models here.
class Utilisateur(models.Model) :
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    mail = models.EmailField(max_length=40,validators=[endsswith])

    def __str__(self):
        return "nom: {}, prenom : {}, mail {}".format(self.nom,self.prenom,self.mail)


class Etudiant(Utilisateur):
    pass
class Coach(Utilisateur):
    pass

class Projet(models.Model):

    nom_projet = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    duree = models.IntegerField('Duree estimee', default=0)
    temps_allouee = models.IntegerField('Temps allouee')
    besoins = models.TextField()
    est_valide = models.BooleanField(default=False)
    createur = models.ForeignKey(Etudiant, on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True, related_name='project_owner')
    superviseur = models.ForeignKey(Coach, on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    related_name='project_coach')
    particpants = models.ManyToManyField(Etudiant,
                                         related_name='les_membres',
                                         blank=True,
                                         through='MembershipInProject')


class MembershipInProject(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps allouee',validators=[MinValueValidator(1),MaxValueValidator(10)])



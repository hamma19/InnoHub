from django.core.exceptions import ValidationError
from django.db import models

def is_esprit_email(value):
    if not str(value).endswith("@esprit.tn"):
        raise ValidationError("Votre Email doit contenir @Esprit.tn", params={'value':value})

class User(models.Model):
    nom = models.CharField('Prenom', max_length=30)
    prenom = models.CharField('Nom', max_length=30)
    email = models.EmailField('Email',validators=[is_esprit_email])

    def __str__(self):
        return "nom: {}, prenom= {}".format(self.nom, self.prenom)


class Student(User):
    pass


class Coach(User):
    pass


class Project(models.Model):
    nom_du_projet = models.CharField('Titre du projet', max_length=30)
    duree_du_projet = models.IntegerField('Duree estimee', default=0)
    temps_alloue_par_le_createur = models.IntegerField('Temps alloue')
    besoins = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    # Validation State of the project
    est_valide = models.BooleanField(default=False)

    createur = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )

    superviseur = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='project_coach'
    )

    membres = models.ManyToManyField(
        Student,
        through='MembershipInProject',
        related_name='les_membres',
        blank=True,
    )

    def __str__(self):
        return self.nom_du_projet


class MembershipInProject(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps allouĂ© par le membre')

    def __str__(self):
        return 'Membre ' + self.etudiant.nom

    class Meta:
        unique_together = ("projet", "etudiant")
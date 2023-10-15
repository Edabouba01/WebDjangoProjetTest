from django.db import models

# Create your models here.
from django.db import models
#La classe nommer etudiant represente un enseignant
#un enseignant peut donner plusieur cours dans mon cas 
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254, default= "Bendemba@gmail.com")
    phone = models.IntegerField(null=True)
    matricule= models.FloatField(default=2088077)
    
    def __str__(self):
            return f"{self.nom}, {self.date_naissance}, {self.email}, {self.phone}, {self.matricule}"
    
class Cour(models.Model):
    titre = models.CharField(max_length=200)
    url= models.URLField(max_length=254, default= "www.google.com")
    description= models.TextField(max_length=254, default= " Dans ce cours, nous allons corriger, ensemble, cette mauvaise posture qui est à lorigine de votre stress, de vos maux de tête et linconfort global que vous ressentez.Jai conçu ce cours de programmation pour qu'il soit accessible aux débutants.")
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE )

    def __str__(self):
            return f"{self.titre}, {self.url}, {self.description}, {self.etudiant}"

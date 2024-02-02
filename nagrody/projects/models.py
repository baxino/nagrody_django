from django.db import models
from django.forms import ModelForm

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    
    

    def __str__(self):
        return self.title
    
    
    
    
class Nagrody(models.Model):
    
    typ_nagrody_slownik={
        "nagrody ministra" : "nagrody ministra właściwego do spraw oświaty i wychowania",
        "nagrody WKO" : "nagrody Wielkopolskiego Kuratora Oświaty"
    }
    
    zajmowane_stanowisko_slownik={
        "dyrektor": "dyrektor",
        "nauczyciel": "nauczyciel (także wicedyrektor)"
    }
    posiadane_wyksztalcenie_slownik={
      "srednie" :  "średnie z przygotowaniem pedagogicznym",
       "srednie_zaklad": "średnie z przygotowaniem pedagogicznym - Zakład kształcenia Nauczycieli",
        "wyzsze" : "wyższe zawodowe z przygotowaniem pedagogicznym"
    }
    
    typ_nagrody=models.CharField(max_length=50,choices=typ_nagrody_slownik)
    imie=models.CharField(max_length=100)
    nazwisko=models.CharField(max_length=100)
    data_ur=models.CharField(max_length=100)
    miejsce_ur=models.CharField(max_length=100)
    zajmowane_stanowisko=models.CharField(max_length=70,choices=zajmowane_stanowisko_slownik)
    posiadane_wyksztalcenie= models.CharField(max_length=70,choices=posiadane_wyksztalcenie_slownik)
    
    def __str__(self):
        return self.typ_nagrody
    
    
    
    
class NagrodyForm(ModelForm):
        class meta:
            model=Nagrody
            fields=["typ_nagrody","imie","nazwisko","data_ur"]
from django import forms
from .models import Nagrody
import logging

logger=logging.getLogger(__name__)
class NagrodyForms(forms.ModelForm):
    class Meta:
        model=Nagrody
        fields="__all__"
       
        
        labels={
          "imie": "Imię osoby wnioskowanej",
          "nazwisko":"Nazwisko osoby wnioskowanej",
          "miejsce_ur" : "miejsce urodzenia",
          "data_ur" : "Data urodzenia"  
        }
        
from django import forms
from .models import Mahcine_reception



class Machine_Search_Form(forms.ModelForm):
    class Meta:
        model=Mahcine_reception
        fields=['MN','MRC']
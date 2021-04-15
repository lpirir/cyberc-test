from django import forms
from .models import LoadFile

class ExcelForm(forms.ModelForm):
    class Meta:
        model = LoadFile
        fields = ['name', 'created', 'file']

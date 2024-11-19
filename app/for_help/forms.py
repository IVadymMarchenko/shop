import re
from django import forms
from .models import ForHelp



class HelpForm(forms.ModelForm):
    name = forms.CharField(max_length=32)
    phone = forms.CharField(max_length=12, min_length=10)
   
    class Meta:
        model = ForHelp
        fields = ['name', 'phone']
        
        
    def clean_name(self):
        data=self.cleaned_data['name']
        
        if not data.isalpha():
            raise forms.ValidationError("м'я повинно складатися лише з букв.")
        return data

    def clean_phone(self):
        data=self.cleaned_data['phone']
        
        if not data.isdigit():
            raise forms.ValidationError("Телефонний номер повинен складатися лише з цифр.")
        pattern=re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Телефонний номер повинен містити 10 цифр.")
        return data
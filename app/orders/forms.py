import re
from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=32)
    phone_number = forms.CharField(max_length=15, min_length=10)
    email = forms.EmailField(max_length=20)
    requires_delivery = forms.ChoiceField(choices=[("0", False), ("1", True)], initial=0,)
    city = forms.CharField(max_length=100, required=True)
    delivery_address = forms.CharField()
    payment = forms.ChoiceField(choices=[("0", False), ("1", True)], initial=0,)
    
    

    def clean_phone_number(self):
        data=self.cleaned_data['phone_number']
        
        if not data.isdigit():
            raise forms.ValidationError("Телефонний номер повинен складатися лише з цифр.")
        pattern=re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Телефонний номер повинен містити 10 цифр.")
        return data
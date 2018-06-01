from django import forms
from django.core.exceptions import ValidationError

class LengthException(Exception):
    pass


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(max_length=50)
    city = forms.ChoiceField(choices=[('Hyderabad', 'Hyd')])
    mobile = forms.CharField(max_length=10)

def clean_name(self):
    data = self.cleaned_data['name']
    if len(data) < 4:
        raise forms.ValidationError("name must 4 char")
        return data

def clean_email(self):
    data = self.cleaned_data['email']
    if not data.endswith(".com"):
        raise forms.ValidationError("email must end with .com")
        return data
def clean_city(self):
    data = self.cleaned_data['city']
    if data == "None":
        raise forms.ValidationError("choose city")
        return data
def clean_mobile(self):
    data = self.cleaned_data["mobile"]
    try:
         if len(data) != 10:
             raise LengthException()
         else:
             data = int(data)
    except LengthException:
        raise forms.ValidationError("Mobile nos must contain 10 characters")
    except:
        raise forms.ValidationError(" mobile should contain digit")
    return data
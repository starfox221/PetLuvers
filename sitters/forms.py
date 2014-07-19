from django import forms

from registration.forms import RegistrationForm

from sitters.models import PET_CHOICES
#from sitters.fields import PhoneField
#I'm guessing this was something that didn't get committed.

class UserTypeRegistrationForm(RegistrationForm):
    is_owner = forms.BooleanField(label="I'm looking for someone to care for my pet!", required=False)
    is_sitter = forms.BooleanField(label="I want to become a host or offer pet services!", required=False)

    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    avatar = forms.ImageField()

    address = forms.CharField(max_length=300, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=30, required=False)
    zip_code = forms.IntegerField(required=False)
    tagline = forms.CharField(max_length=40, label="Short 40 character Description")
    description = forms.CharField(max_length=3000, label="Long about you", help_text="", widget=forms.Textarea())
    price = forms.DecimalField(label="Price Per Night Per Pet", decimal_places=2, max_digits=10, required=False)
    pet_types = forms.MultipleChoiceField(label="Pet Types willing to sit", choices=PET_CHOICES, widget=forms.CheckboxSelectMultiple)
    qualifications = forms.CharField(label="Any special qualifications?", required=False)
    not_willing_to_sit = forms.CharField(label="Please describe any animals you would not be willing to sit")
    concerns = forms.CharField(label="Please describe any other concerns")

    pets = forms.CharField(required=False)

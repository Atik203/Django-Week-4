from django import forms
from django.core import validators

from .models import Student


def phone_validator(value):
    if len(value) != 11:
        raise forms.ValidationError('Phone number must be 11 digits')

class DjangoForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,help_text="Type your name",widget=forms.TextInput(attrs={'placeholder':'Your Name...','class':'fw-semibold text-uppercase'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'fw-semibold','placeholder':'Your Email...'}))
    phone = forms.CharField( max_length=11, required=False,label='Phone',validators=[phone_validator],error_messages={'required':'phone number is required'})
    birthday = forms.DateField(label="Birthday",widget=forms.DateInput(attrs={'type':'date'}),required=False)
    Appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),required=False)
    check_box = forms.BooleanField(label='Agree',required=False)
    CHOICES = [('1','First'),('2','Second'),('3','Third')]
    radio = forms.ChoiceField(choices=CHOICES,required=False)
    MULTICHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    checkbox = forms.MultipleChoiceField(choices=MULTICHOICES,required=False,widget=forms.CheckboxSelectMultiple())
    file = forms.FileField(required=False,label='file')
    message = forms.CharField(label='Message', widget=forms.Textarea,required=False)
    
    



class Model_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name':'Your Name',
            'email':'Your Email',
            'phone':'Your Phone',
            'birthday':'Your Birthday',
            'subject':'Your Subject',
            'roll':'Your Roll',
            'city':'Your City',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'fw-semibold text-uppercase'}),
            'email':forms.EmailInput(attrs={'class':'fw-semibold'}),
            'phone':forms.TextInput(attrs={'class':'fw-semibold'}),
            'birthday':forms.DateInput(attrs={'type':'date'}),
            'subject':forms.Select(attrs={'class':'fw-semibold'}),
            'roll':forms.NumberInput(attrs={'class':'fw-semibold'}),
            'city':forms.TextInput(attrs={'class':'fw-semibold'}),
        }
        error_messages = {
            'name':{
                'required':'Name is required'
            },
            'email':{
                'required':'Email is required'
            },
            'phone':{
                'required':'Phone is required'
            },
            'subject':{
                'required':'Subject is required'
            },
            'roll':{
                'required':'Roll is required'
            },
        }
        
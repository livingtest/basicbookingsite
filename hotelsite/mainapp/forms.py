from django import forms
from.models import Contact, Properties, Reservation
from django.core import validators


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
       model=Reservation
       fields='__all__'
       exclude=('room',)
       widgets = {
        'checkin':DateInput(attrs={'class':  'form-control datepicker'}),
        'checkout':DateInput(attrs={'class': 'form-control datepicker'}),
        'email':forms.EmailInput( attrs={'class': 'form-control datepicker'}),
        'fullname':forms.TextInput(attrs={'class': 'form-control'}),
        'phone':forms.TextInput(attrs={'class': 'form-control'}),

       
        


        }
  
    
    


       

class ContactForm(forms.ModelForm):

    class Meta:
       model=Contact
       fields='__all__'
      
       widgets = {
        
        'fullname':forms.TextInput(attrs={'class': 'form-control'}),
        'subject':forms.TextInput(attrs={'class': 'form-control'}),
        'email':forms.EmailInput( attrs={'class': 'form-control datepicker'}),
        'message':forms.Textarea(attrs={'class': 'form-control'}),

       
        


        }


  

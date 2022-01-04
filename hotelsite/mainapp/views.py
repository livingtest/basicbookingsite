from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Agents, Contact, Properties,Categories,Reservation
from  .forms import ContactForm, ReservationForm
from django.core.mail import message, send_mail,BadHeaderError,EmailMessage

# Create your views here.


def home(request):
    homelisting=Properties.objects.all()[:3]
    context={
        
        
        'listproperty':homelisting
        
        }
    return render(request,'index.html',context)




def propertylist(request):
    listing=Properties.objects.all()
    context={
        
        
        'listproperty':listing
        
        }

    return render(request,'property/properties.html',context)





def property_detail(request,id):

   detailofproperty=Properties.objects.get(id=id)
   newname=detailofproperty
 
  

   if request.method == 'POST':
       reserve_form=ReservationForm(request.POST)


       if reserve_form.is_valid():
            fullname=reserve_form.cleaned_data['fullname']
            checkin =reserve_form.cleaned_data['checkin']
            checkout = reserve_form.cleaned_data['checkout']
            email=reserve_form.cleaned_data['email']
            phone=reserve_form.cleaned_data['phone']

            reserve_form= Reservation.objects.create(
                checkin=checkin, checkout=checkout,room=newname,email=email,phone=phone,fullname=fullname)
           

            
        


            try:
                
                subject="Thank you for choosing us"
                message="We will call you soon for comfirmation"
                mainmail='axumono@gmail.com'
                send_mail(subject,message,mainmail,[email])
                reserve_form.save()
               
                
                

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('booked')
    
   
    
   else:
        reserve_form=ReservationForm()

		
   context={

       'listproperty':detailofproperty,
       'reserve' : reserve_form,

   }
   return render(request,'property/detail.html',context)


def booked(request):
   

    
    
    return render(request,'booked.html')



def about(request):
 

    return render(request,'about.html')



def contact(request):

    contact_form=ContactForm()
    
    if request.method =='POST':
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            fullname=contact_form.cleaned_data['fullname']
            email=contact_form.cleaned_data['email']
            message=contact_form.cleaned_data['message']
            subject=contact_form.cleaned_data['subject']

            contact_form= Contact.objects.create(
              fullname=fullname, email=email,message=message,subject=subject)
           
            
            
            try:
                contact_form.save()
                send_mail(subject,message,email,['axumono@gmail.com'])
                
                

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    
    else:
        contact_form=ContactForm()
    


    context={'contact':contact_form}

    return render(request,"contact.html",context)



def agents(request):
    agents_list=Agents.objects.all()
    
    return render(request,'agents.html',context={'agentoflist':agents_list})
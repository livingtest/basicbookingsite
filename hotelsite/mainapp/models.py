from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import AutoField, TextField



# Create your models here.
roomtype =(
    ( "Alpha" ,"A") ,
    ("Beta","B" ),
    ( "Classy","C"),
    ( "Luxury","L"),
)


class Categories(models.Model):
    categories=models.CharField(max_length=25)



    def __str__(self):
        return self.categories



    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'




class Properties(models.Model):
    categories=models.ForeignKey(Categories,null=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    type= models.CharField(choices=roomtype,max_length=25)
    price=models.PositiveIntegerField()
    area=models.DecimalField(decimal_places=2,max_digits=10)
    numofbeds=models.PositiveIntegerField()
    numofbath=models.PositiveIntegerField()
    numofgarage=models.CharField(max_length=10)
    photo = models.ImageField(upload_to='rooms',null=True)
    roomdetail=models.TextField(max_length=255,default=True)

    def __str__(self):
        return f"{self.numofbeds} beds and {self.numofbath} baths located at {self.location}"



    class Meta:
        verbose_name='Property'
        verbose_name_plural='Properties'




class Reservation(models.Model):

    fullname=models.CharField(max_length=100)
    room=models.ForeignKey(Properties,null=False,on_delete=models.CASCADE)
    checkin=models.DateField()
    checkout=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=13,default='+233')







    def __str__(self):
        return f"Reserve {self.room} for {self.fullname}"




class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField()
    message=models.TextField(max_length=255)


    def __str__(self):
        return self.email


class Agents(models.Model):
    fullname=models.CharField(max_length=100)
    numoflisting=models.IntegerField()
    agentdescription=models.TextField(max_length=255)
    agentphoto=models.ImageField(upload_to='agents',null=False)



    class Meta:
        verbose_name='agent'
        verbose_name_plural='agents'

    def __str__(self):
      return  self.fullname
        
  
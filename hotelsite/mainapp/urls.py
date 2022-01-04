
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

     path('',views.home,name='home'),
     path('property/',views. propertylist,name='propertylist'),
     path('<int:id>/',views.property_detail,name='detail'),
     path('booked/',views.booked,name='booked'),
     path('agents',views.agents,name='agents'),
    
     path('about',views.about,name='about'),
     path('contact',views.contact,name='contact'),

    
  
 ]
 
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



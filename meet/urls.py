from django.urls import path
from . import  views
urlpatterns=[
    path('',views.index),
    path('<slug:meet_slug>/success',views.confirm_registration, name='confirm-registration'),
    path('<slug:meet_slug>',views.meet_detail, name='meet-detail'),
    
    
]



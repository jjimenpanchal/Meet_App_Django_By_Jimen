from django.shortcuts import render, HttpResponse, redirect
from.models import Meet, Participant
from .forms import RegistrationForm
# Create your views here.
def index(request):
    meets=Meet.objects.all()
    return render(request,"meet/index.html",
    {
        'meets':meets
    })

def meet_detail(request,meet_slug):

    selected_meet=Meet.objects.get(slug=meet_slug)
    try:
        if request.method=='GET':
            registration_form=RegistrationForm()
            
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant=registration_form.save()
                user_email=registration_form.cleaned_data['email']
                participant,was_created= Participant.objects.get_or_create(email=user_email)
                selected_meet.Participants.add(participant)
                return redirect("confirm-registration",meet_slug=meet_slug)
        return render (request,'meet/meet-detail.html',
            {
                'meet':selected_meet,
                'meet_found':True,
                'form':registration_form
            })
    except Exception as e:
        print('Exceptio is :: ',e)  
        return render (request,'meet/meet-detail.html',
        {
           
            'meet_found':False
        })

def confirm_registration(request,meet_slug ):
    meet=Meet.objects.get(slug=meet_slug)
    # return HttpResponse("done dona done ")
    return render (request,'meet/registration_success.html',{
        'organizer_email':meet.organizer_email
    })

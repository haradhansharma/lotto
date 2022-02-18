from django.contrib import messages
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from .models import *
from .forms import UserCreationFormFront
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator




def signup(request):       
        
    if request.method == 'POST':
        current_site = get_current_site(request)
        form = UserCreationFormFront(request.POST)
        if form.is_valid():     
            new_user = form.save(commit=False)    
            new_user.is_active = False       
            new_user.save()
            subject = 'Account activation required!'                  
            
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('emails/account_activation_email.html', {
                'user': new_user,                    
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
                
            })
            
            new_user.email_user(subject, message)
            
            messages.success(request, 'Please Confirm your email to complete registration.') 
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else: 
        form = UserCreationFormFront()
    context = {
        'form': form,      
        
    }
    return render(request, 'registration/register.html', context = context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, ('Your account have been confirmed.'))
        return HttpResponseRedirect(reverse_lazy('login'))
    else:
        messages.warning(request, ('Activation link is invalid!'))
        return HttpResponseRedirect(reverse_lazy('home:home'))
        
    
@login_required
def userpage(request, username):
    context = {}
    return render(request, 'registration/userpage.html', context = context)



    
    
    
    
    
    
    


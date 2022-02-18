from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .forms import UserForm, ProfileForm, PasswordChangeForm, ProfilePictureForm, ProfileCoverForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from accounts.models import User
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Min
from .forms import LoginFormFront
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.tokens import account_activation_token
from django import forms


def home(request):
    
    
    
    form = LoginFormFront(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if email and password:
                email_qs = User.objects.filter(email=email)
                if not email_qs.exists():                    
                    messages.error(request, 'The user does not exist')
                else:
                    is_active_qs = User.objects.filter(email=email, is_active=False).first()
                    if is_active_qs:
                        subject = 'Account activation required!'  
                        current_site = Site.objects.get_current()  
                        message = render_to_string('emails/account_activation_email.html', {
                            'user': is_active_qs,                    
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(is_active_qs.pk)),
                            'token': account_activation_token.make_token(is_active_qs),                        
                        })
                        is_active_qs.email_user(subject, message)  
                        messages.error(request, f'Account is not active, your need to activate your account before login. An account activation link has been sent to your mailbox {email}')              
                    else:
                        user = authenticate(email=email, password=password)  
                        if not user:                            
                            messages.error(request, 'Incorrect password. Please try again!')
                        else:
                            login(request, user)
                            return HttpResponseRedirect(reverse('home:dashboard')) 
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    
    context = {
        'form': form
        
        
             
    }
    return render(request, 'home/index.html', context = context)





    


@login_required
def dashboard(request):    
    context = {}       
    return render(request, 'home/dashboard.html', context = context)


@login_required
def calender(request):    
    context = {}       
    return render(request, 'home/calendar.html', context = context)


@login_required
def components_form(request):    
    context = {}       
    return render(request, 'home/components-forms.html', context = context)


@login_required
def components_model(request):    
    context = {}       
    return render(request, 'home/components-modals.html', context = context)


@login_required
def components_notifications(request):    
    context = {}       
    return render(request, 'home/components-notifications.html', context = context)

@login_required
def components_typography(request):    
    context = {}       
    return render(request, 'home/components-typography.html', context = context)



@login_required
def all_traffic(request):    
    context = {}       
    return render(request, 'home/dashboard-traffic-sources.html', context = context)


@login_required
def product_analysis(request):    
    context = {}       
    return render(request, 'home/dashboard-app-analysis.html', context = context)


@login_required
def kanban(request):    
    context = {}       
    return render(request, 'home/kanban.html', context = context)


@login_required
def message(request):    
    context = {}       
    return render(request, 'home/messages.html', context = context)


@login_required
def users(request):    
    context = {}       
    return render(request, 'home/users.html', context = context)

@login_required
def transactions(request):    
    context = {}       
    return render(request, 'home/transactions.html', context = context)




@login_required
def tasks(request):    
    context = {}       
    return render(request, 'home/tasks.html', context = context)



@login_required
def map(request):    
    context = {}       
    return render(request, 'home/map.html', context = context)



@login_required
def datatables(request):    
    context = {}       
    return render(request, 'home/tables-datatables.html', context = context)



@login_required
def bootstrap_tables(request):    
    context = {}       
    return render(request, 'home/tables-bootstrap-tables.html', context = context)


@login_required
def pricing(request):    
    context = {}       
    return render(request, 'home/page-pricing.html', context = context)


@login_required
def billing(request):    
    context = {}       
    return render(request, 'home/page-billing.html', context = context)




@login_required
def invoice(request):    
    context = {}       
    return render(request, 'home/page-invoice.html', context = context)
@login_required
def page_signin(request):    
    context = {}       
    return render(request, 'home/page-sign-in.html', context = context)
@login_required
def page_signup(request):    
    context = {}       
    return render(request, 'home/page-sign-up.html', context = context)
@login_required
def page_forget_password(request):    
    context = {}       
    return render(request, 'home/page-forgot-password.html', context = context)
@login_required
def page_reset_password(request):    
    context = {}       
    return render(request, 'home/page-reset-password.html', context = context)
@login_required
def page_lock(request):    
    context = {}       
    return render(request, 'home/page-lock.html', context = context)
@login_required
def page_404(request):    
    context = {}       
    return render(request, 'home/page-404.html', context = context)

@login_required
def page_500(request):    
    context = {}       
    return render(request, 'home/page-500.html', context = context)

@login_required
def buttons(request):    
    context = {}       
    return render(request, 'home/components-buttons.html', context = context)

@login_required
def widgets(request):    
    context = {}       
    return render(request, 'home/widgets.html', context = context)

@login_required
def page_404(request):    
    context = {}       
    return render(request, 'home/page-404.html', context = context)

@login_required
def lotto(request):    
    context = {}       
    return render(request, 'home/lotto.html', context = context)

@login_required
def sports(request):    
    context = {}       
    return render(request, 'home/sports.html', context = context)

@login_required
def crypto(request):    
    context = {}       
    return render(request, 'home/crypto.html', context = context)




@login_required
def user_setting(request):   
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
        profile_picture_form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)        
        profile_cover_form = ProfileCoverForm(request.POST, request.FILES, instance=request.user.profile)
        if 'user_form' in request.POST or 'profile_form' in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request,('Your profile was successfully updated!'))		    
            elif profile_form.is_valid():
                profile_form.save()
                messages.success(request,('Your profile data was successfully updated!'))
            else:
                messages.error(request, 'Invalid form submission.')
                messages.error(request, profile_form.errors)
                messages.error(request, user_form.errors)
        if 'profile_picture_form' in request.POST:
            if profile_picture_form.is_valid():
                profile_picture_form.save()
                messages.success(request,('Your profile was successfully updated!'))
                
        if 'profile_cover_form' in request.POST:
            if profile_cover_form.is_valid():
                profile_cover_form.save()
                messages.success(request,('Your profile was successfully updated!'))
           
           
        
        return HttpResponseRedirect(reverse('home:user_settings'))
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    profile_picture_form = ProfilePictureForm()        
    profile_cover_form = ProfileCoverForm()    
    
    context = {
        "user":request.user,
        "user_form":user_form,
        "profile_form":profile_form,
        'profile_picture_form': profile_picture_form,
        'profile_cover_form': profile_cover_form
        
    }
    return render(request, 'home/settings.html', context = context)

@login_required
def password_change(request):   
    
    if request.method == "POST":        
        password_form = PasswordChangeForm(user=request.user, data=request.POST)        
        if password_form.is_valid():            
            password_form.save()            
            update_session_auth_hash(request, password_form.user)            
            messages.success(request,('Your password was successfully updated!')) 
        else:
            messages.error(request, 'Invalid form submission.')            
            messages.error(request, password_form.errors)       
        
        return HttpResponseRedirect(reverse('home:dashboard'))
    
    password_form = PasswordChangeForm(request.user)  
    
    context = {
        "user":request.user,        
        "password_form":password_form
    }
    return render(request, 'home/page-reset-password.html', context = context)













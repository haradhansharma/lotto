from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import User
from .tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        
        
        
class UserCreationFormFront(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control" }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control" }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password check","class": "form-control"}))
    
    
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        
        if email and password:
            email_qs = User.objects.filter(email=email)
            if not email_qs.exists():
                pass    
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
                    raise forms.ValidationError(f'You have an account already with this email. An account activation link has been sent to your mailbox {email}')  
            
                              
            
                
                                    
        return super(UserCreationFormFront, self).clean(*args, **kwargs)    

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control" }))    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    
    
    def clean(self, *args, **kwargs):
        
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            email_qs = User.objects.filter(email=email)
            if not email_qs.exists():
                raise forms.ValidationError("The user does not exist")
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
                    
                    raise forms.ValidationError(f'Account is not active, your need to activate your account before login. An account activation link has been sent to your mailbox {email}')                
                else:
                    user = authenticate(email=email, password=password)  
                    if not user:
                        raise forms.ValidationError("Incorrect password. Please try again!")
                
                                    
        return super(LoginForm, self).clean(*args, **kwargs)
    

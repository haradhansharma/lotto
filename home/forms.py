from django import forms
from accounts.models import User, Profile
from django.contrib.auth.forms import PasswordChangeForm


class LoginFormFront(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class':'form-control'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})
        





class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'orgonization', 'phone', )
        
        widgets = {
                      
            'username': forms.TextInput(attrs={'placeholder': 'username', 'class':'form-control', 'aria-label':'username',  }),
            'first_name': forms.TextInput(attrs={'placeholder': 'first_name', 'class':'form-control', 'aria-label':'first_name' }),
            'last_name': forms.TextInput(attrs={'placeholder': 'last_name','class':'form-control', 'aria-label':'last_name', }), 
            'orgonization': forms.TextInput(attrs={'placeholder': 'orgonization','class':'form-control', 'aria-label':'orgonization', }), 
            'phone': forms.TextInput(attrs={'placeholder': 'phone','class':'form-control', 'aria-label':'phone', }), 
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class':'form-control', 'aria-label':'email' , }),
            
            
        }
        labels = {     
                     
            'username':'Username',
            'first_name':'First name',
            'first_name':'Last Name',
            'orgonization':'Orgonization',
            'phone':'Phone',
            'email': 'Email',
            
        }
        
        
   
        
class ProfileForm(forms.ModelForm):
    class Meta:   
        
        model = Profile
        fields = ('about',)
        
        widgets = {                      
            'about': forms.Textarea(attrs={'placeholder': 'about', 'class':'form-control', 'aria-label':'about' }),
                        
        }
        labels = {    
                     
            'about': 'About',                 
            
        }
        
class ProfilePictureForm(forms.ModelForm):
    class Meta:   
        
        model = Profile
        fields = ('profile_photo',)
        
        # widgets = {                      
        #     'profile_photo': forms.ImageField(attrs={'placeholder': 'about', 'class':'form-control', 'aria-label':'about' }),
                        
        # }
        
class ProfileCoverForm(forms.ModelForm):
    class Meta:   
        
        model = Profile
        fields = ('cover_photo',)
        
        # widgets = {                      
        #     'cover_photo': forms.ImageField(attrs={'placeholder': 'about', 'class':'form-control', 'aria-label':'about' }),
                        
        # }
        
        


        
       
  
  
        
  
  
       
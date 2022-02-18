
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView 
from .forms import LoginForm


app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',  LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm ),  name='login'),
    
    
    
]

urlpatterns += [
    path('<str:username>', views.userpage, name='user_link'),
    
]

urlpatterns += [
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    
]




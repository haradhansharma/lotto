from . import views
from django.urls import path



app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/settings/', views.user_setting, name='user_settings'),
    path('dashboard/change_pass/', views.password_change, name='change_pass'),    
]


urlpatterns += [
    path('dashboard/calender/', views.calender, name='calender'),    
    path('dashboard/components_form/', views.components_form, name='components_form'),    
    path('dashboard/components_model/', views.components_model, name='components_model'),    
    path('dashboard/components_notifications/', views.components_notifications, name='components_notifications'),    
    path('dashboard/components_typography/', views.components_typography, name='components_typography'), 
]


urlpatterns += [
    path('dashboard/all_traffic/', views.all_traffic, name='all_traffic'),    
    path('dashboard/product_analysis/', views.product_analysis, name='product_analysis'),    
    path('dashboard/kanban/', views.kanban, name='kanban'),    
    path('dashboard/message/', views.message, name='message'),    
    path('dashboard/users/', views.users, name='users'), 
]


urlpatterns += [
    path('dashboard/transactions/', views.transactions, name='transactions'),    
    path('dashboard/tasks/', views.tasks, name='tasks'),    
    path('dashboard/map/', views.map, name='map'),    
    path('dashboard/datatables/', views.datatables, name='datatables'),    
    path('dashboard/bootstrap_tables/', views.bootstrap_tables, name='bootstrap_tables'), 
]


urlpatterns += [
    path('dashboard/pricing/', views.pricing, name='pricing'),    
    path('dashboard/billing/', views.billing, name='billing'),    
    path('dashboard/invoice/', views.invoice, name='invoice'),    
    path('dashboard/page_signin/', views.page_signin, name='page_signin'),    
    path('dashboard/page_signup/', views.page_signup, name='page_signup'), 
]

urlpatterns += [
    path('dashboard/page_forget_password/', views.page_forget_password, name='page_forget_password'),    
    path('dashboard/page_reset_password/', views.page_reset_password, name='page_reset_password'),    
    path('dashboard/page_lock/', views.page_lock, name='page_lock'),    
    path('dashboard/page_404/', views.page_404, name='page_404'),    
    path('dashboard/page_500/', views.page_500, name='page_500'), 
]

urlpatterns += [
    path('dashboard/buttons/', views.buttons, name='buttons'),    
    path('dashboard/widgets/', views.widgets, name='widgets'),    
    path('dashboard/page_lock/', views.page_lock, name='page_lock'),    
    path('dashboard/page_404/', views.page_404, name='page_404'),    
    path('dashboard/page_500/', views.page_500, name='page_500'), 
]


urlpatterns += [
    path('dashboard/lotto/', views.lotto, name='lotto'),    
    path('dashboard/sports/', views.sports, name='sports'),    
    path('dashboard/crypto/', views.crypto, name='crypto'),    
    
]






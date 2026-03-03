from django.contrib import admin
from django.urls import path, include
from tasks.forms import BootstrapAuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('tasks.urls')),

    path(
    'login/',
    auth_views.LoginView.as_view(
        authentication_form=BootstrapAuthenticationForm
    ),
    name='login'
),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
]
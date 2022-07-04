
from django.contrib import admin
from django.urls import path
from service.views import user_login_view, user_register_view, profile

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', user_login_view, name='login'),
    path('', user_register_view, name='register'),
    path('profile/', profile, name='profile'),
]

from django.urls import path
from .views import index, log_out, performan,sign_up,sign_in

urlpatterns = [
    path('', index,name="index"),
    path('sign-up/', sign_up ,name='sign-up'),
    path('sign-in/', sign_in ,name='sign-in'),
    path('sign-in/resetpassword', sign_in ,name='sign-in-resetpw'),
    path('log-out/', log_out ,name='log-out'),
    path('performance/',performan,name='performance')
]

from django.urls import path
from .views import SignUpView, MyLoginView, MyLogoutView


app_name = 'users'


urlpatterns = [
    path('registration/', SignUpView.as_view(), name='user_create'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
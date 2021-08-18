from django.urls import path, re_path
from . import views

app_name = 'L5P_App'

urlpatterns = [
    re_path('^register/$', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('specials/', views.special_view,name='specials'),
]

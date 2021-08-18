"""Level5Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from L5P_App import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('admin/', admin.site.urls),
    re_path(r'^L5P_App/', include('L5P_App.urls')),
    path('logout/', views.user_logout, name='logout'),
    #path('specials/', views.special_view, name='specials')
]

'''
    To make images uploaded from front accessible in the Admin section, added these lines -
'''
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    Image accessible in the admin...
'''
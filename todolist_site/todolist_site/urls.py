"""todolist_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from todolist_app.views import Login, Logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/logout/$', Logout.as_view(), name='logout'),
    url(r'^accounts/login/$', Login.as_view(), name='login'),
    # url(r'^password_reset/$', Login, name='password_reset'),
    url(r'', include('todolist_app.urls')),
    url('', include('social_django.urls', namespace='social')),
    url(r'tasks/', include('todolist_app.urls')),
]

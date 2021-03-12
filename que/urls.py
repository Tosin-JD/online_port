"""que URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

from accounts.views import ThanksPage
from ship.views import HomePage
from services.views import AboutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('thanks/', ThanksPage.as_view()),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('services/', include('services.urls', namespace='services')),
    path('', include('ship.urls', namespace='ship')),
]


if settings.DEBUG:
    urlpatterns +=[re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT
    })
        ]



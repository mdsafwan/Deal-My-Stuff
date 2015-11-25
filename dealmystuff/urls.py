"""dealmystuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login.views import display_login, after_login, login, login_user, register, logout, login_error, logged_in
from advertisements.views import home, post_advertisement, display_advertisement, product_display, advertisement_select_category,\
    contact_us
from django.conf import settings
from django.conf.urls import patterns

# ... your normal urlpatterns here


urlpatterns = [
    url(r'^login2/$', login_user),
    url(r'^register/$', register),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^login_error/', login_error),
    url(r'^logged_in/', logged_in),
    url(r'^contact_us/', contact_us),
    url(r'^home/', home),
    url(r'^after_login/', after_login),
    url(r'^post_advertisement/', post_advertisement),
    url(r'^post_advertisement_select_category', advertisement_select_category),
    url(r'^display_advertisement/', display_advertisement),
    url(r'^product_display/', product_display),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),)
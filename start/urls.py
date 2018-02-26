from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # url(r'^$', views.login, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # url(r'^v_login', views.val_login, name='v_login'),
    # url(r'^logout', views.logout, name='logout'),
    # url(r'^password_change', views.pchange, name='pass_change'),
    # url(r'^password_reset', views.preset, name='pass_reset'),
    # url(r'^dashboard', views.dashboard, name='dashboard'),
]
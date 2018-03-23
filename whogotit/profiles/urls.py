from django.conf.urls import  include, url
from . import views,html_views


urlpatterns = [
    url(r'^session/$', views.SessionCheck, name='api_session_check'),
    url(r'^login/$', views.account_login, name='api_account_login'),
    url(r'^logout/$', views.account_logout, name='api_account_logout'),
    url(r'^signin/$', views.account_signin, name='api_account_signin'),
    url(r'^password/reset/$', views.account_password_reset_request_key, name='api_account_password_reset_request_key'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', views.account_password_reset_from_key, name='api_account_password_reset_from_key'),
    url(r'^account/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$',html_views.password_reset_from_key,name='account_password_reset_from_key'),
    url(r'^user_profile/$', views.user_profile_list ,name='user_profile_list'),
    url(r'^user_profile/(?P<user>[-\w.]+)/$', views.user_profile_detail ,name='user_profile_detail'),
]


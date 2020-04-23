from django.conf.urls import url
from . import views as norm_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^register/$', norm_views.registration_view, name='register'),
    url(r'^login/$', norm_views.login_view, name='login'),
    url(r'^logout/$', norm_views.logout_view, name='logout'),
    url(r'^account/update/$', norm_views.account_update, name='account-update'),
    url(r'^account/details/$', norm_views.account_view, name='account'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name='password-change-complete'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name='password-change'),
    url(r'^password_reset/done/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_done.html'),
        name='password-reset-done'),
    url(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',
                                             email_template_name='account/password_reset_email.html'),
        name='password-reset'),
    url(r'^reset/<uidb64>/<token>//$', auth_views.PasswordResetConfirmView.as_view(),
        name='password-reset-confirm'),
    url(r'^reset_done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password-reset-complete'),

]

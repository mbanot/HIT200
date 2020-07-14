from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

from .forms import AccountRegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account


def registration_view(request):
    template_name = 'account/register.html'
    context = {}
    if request.POST:
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('auction:index')
        else:
            context['form'] = form
    else:
        form = AccountRegistrationForm
        context['form'] = form
    return render(request, template_name, context)


def login_view(request):
    template_name = 'account/login_form.html'
    context = {}

    user = request.user
    if user.is_authenticated:
        redirect('auction:index')

    if request.POST:
        form = AccountAuthenticationForm()
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('auction:index')
    else:
        form = AccountAuthenticationForm()

    context['form'] = form
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('account:login')


def account_view(request):
    template_name = 'account/account_details.html'
    context = {'account': request.user}
    return render(request, template_name, context)


def account_update(request):

    if not request.user.is_authenticated:
        return redirect('account:login')

    template_name = 'account/account_form.html'
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
        template_name = 'account/account_details.html'
        context['account'] = request.user

    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )
        context['form'] = form
    return render(request, template_name, context)


def password_reset_done(request,
                        template_name='registration/password_reset_done.html',
                        current_app=None, extra_context=None):
    context = {
        'title': _('Password reset sent'),
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

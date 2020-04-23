from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountRegistrationForm(UserCreationForm):

    YEARS = [x for x in range(1900, 2020)]
    email = forms.EmailField(max_length=60, help_text='Required field. Add a valid email address.')
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Account
        field = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name',
                 'date_of_birth', 'profile_picture', 'phone_number', 'residential_address', 'city', 'country']
        exclude = ['is_active', 'is_admin', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'password']


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name']

    def clean_email(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'phone_number', 'residential_address',
                    'city', 'country', 'date_joined', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
# admin.site.site_title = 'Auction'
# admin.site.site_header = 'Auction'
# admin.site.index_title = 'Welcome '


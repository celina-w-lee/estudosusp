from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import MyUser

class MyUserAdmin(BaseUserAdmin):
    list_display = ('name', 'nusp', 'email', 'is_admin', 'is_active')
    search_fields = ('name', 'nusp', 'email')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('name', 'nusp', 'email', 'password1', 'password2'),
        }),
    )

    ordering = ('name',)



admin.site.register(MyUser, MyUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Globally disable 'delete selected' action
admin.site.disable_action('delete_selected')

# Defining custom actions


def soft_delete(self, request, queryset):
    queryset.delete()


def restore(self, request, queryset):
    queryset.restore()


def hard_delete(self, request, queryset):
    queryset.delete(force=True)


admin.site.add_action(restore, "Restore deleted Objects", )
admin.site.add_action(soft_delete, "Delete temporary Objects", )
admin.site.add_action(hard_delete, "Delete permanently Objects", )
actions = ["restore", "soft_delete", "hard_delete", ]


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'first_name', 'last_name',
                    'username', 'email', 'is_staff', 'is_active',)


admin.site.register(CustomUser, CustomUserAdmin)

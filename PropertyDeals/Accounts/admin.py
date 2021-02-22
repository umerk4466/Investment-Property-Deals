from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# import models
from .models import Profile
from .models import User


# display profile inside of user model in admin panel
class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    # add field which created in custom User model
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            None,  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'user_type',
                ),
            },
        ),
    )
    

# Register all the models in admin panel
admin.site.register(User, CustomUserAdmin)
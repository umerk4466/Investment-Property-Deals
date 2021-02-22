from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# import models
from .models import Profile
from .models import User
from .models import DealSourcer
from .models import Admin




# display profile inside of user model in admin panel
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

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
admin.site.register(DealSourcer)
admin.site.register(Admin)
admin.site.register(Profile)


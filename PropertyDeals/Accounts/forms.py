from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User




# investor signup form
class InvestorSignup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(InvestorSignup, self).__init__(*args, **kwargs)
        # below changing on the fields of this form.
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

    post_code = forms.CharField(label="Post Code", max_length=255)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'post_code', 'username', 'password1', 'password2' ]

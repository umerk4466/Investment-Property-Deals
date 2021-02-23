from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User


# login form
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # specify field's placeholder
        self.fields['username'].widget.attrs["placeholder"] ="Enter Your Username"
        self.fields['password'].widget.attrs["placeholder"] ="Enter Your Password"
        # remove labels from fields
        self.fields['username'].label = ""
        self.fields['password'].label = ""

# investor signup form
class InvestorSignup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(InvestorSignup, self).__init__(*args, **kwargs)
        # remove labels from fields
        for fieldname in ['first_name', 'last_name','username', 'password1', 'password2']:
            self.fields[fieldname].label = ""
        # specify field's placeholder
        self.fields['first_name'].widget.attrs["placeholder"] ="First Name (Optional)"
        self.fields['last_name'].widget.attrs["placeholder"] ="Last Name (Optional)"
        self.fields['username'].widget.attrs["placeholder"] ="Username"
        self.fields['password1'].widget.attrs["placeholder"] ="Password"
        self.fields['password2'].widget.attrs["placeholder"] ="Confirm Password"
        # remove help text from fields
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None


    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'password1', 'password2' ]

# deal sourcer signup form
class DealSourcerSignup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(DealSourcerSignup, self).__init__(*args, **kwargs)
        # below changing on the fields of this form.
        self.fields['email'].required = True
        # remove labels from fields
        for fieldname in ['first_name', 'last_name','email','username', 'password1', 'password2']:
            self.fields[fieldname].label = ""
        # specify field's placeholder
        self.fields['first_name'].widget.attrs["placeholder"] ="First Name (Optional)"
        self.fields['last_name'].widget.attrs["placeholder"] ="Last Name (Optional)"
        self.fields['username'].widget.attrs["placeholder"] ="Username"
        self.fields['email'].widget.attrs["placeholder"] ="Email Address"
        self.fields['password1'].widget.attrs["placeholder"] ="Password"
        self.fields['password2'].widget.attrs["placeholder"] ="Confirm Password"
        # remove help text from fields
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None

    post_code = forms.CharField(label='',max_length=255, 
                    widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'post_code', 'username', 'password1', 'password2' ]

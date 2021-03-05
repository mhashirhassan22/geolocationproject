from allauth.account.forms import LoginForm, SignupForm
from django import forms


class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget = forms.TextInput(
            attrs={"type": "email", "class": "form-control", "placeholder": "Email"}
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )


class YourSignupForm(SignupForm):
    name = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(YourSignupForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget = forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name"}
        )
        self.fields["email"].widget = forms.TextInput(
            attrs={"type": "email", "class": "form-control", "placeholder": "Email"}
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Password",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )

    def save(self, request):
        user = super(YourSignupForm, self).save(request)

        # Add your own processing here.
        user.name = self.cleaned_data["name"]
        user.save()
        # You must return the original result.
        return user

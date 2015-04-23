from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = SignUp
        fields = "__all__"
        widgets = {
                   'password': forms.PasswordInput(),
                   }
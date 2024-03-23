from django import forms
from .models import Messages, Templates
from django.contrib.auth.models import User


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ["title", "content", "recipients"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                    "required": True,
                    "type": "text",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Content",
                    "required": True,
                    "type": "text",
                    "rows": 5,
                    "cols": 7,
                }
            ),
            "recipients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recipients e.g +23370000 +23370000",
                    "required": True,
                    "type": "text",
                    "rows": 5,
                    "cols": 7,
                }
            ),
        }


class TemplatesForm(forms.ModelForm):
    class Meta:
        model = Templates
        fields = ["title", "content", "recipients"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "cols": 7}
            ),
            "recipients": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "cols": 7}
            ),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "type": "text",
                    "placeholder": "Username",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "type": "password",
                    "placeholder": "Password",
                }
            ),
        }

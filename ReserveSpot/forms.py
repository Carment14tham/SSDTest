from django import forms

class LoginForm(forms.Form):
    uname = forms.CharField(label="uname", max_length=150)
    psw = forms.CharField(label="psw", widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    uname = forms.CharField(label="uname", max_length=150)
    email = forms.EmailField(label="email")
    psw = forms.CharField(label="psw", widget=forms.PasswordInput())

class ProfileForm(forms.Form):
    nameinfo = forms.CharField(label="nameinfo", max_length=150)
    emailinfo = forms.EmailField(label="emailinfo")
    phoneinfo = forms.CharField(label="phoneinfo", max_length=8)
    pwdinfo = forms.CharField(label="pwdinfo", widget=forms.PasswordInput())

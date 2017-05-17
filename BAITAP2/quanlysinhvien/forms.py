from django import forms

class RegisterForm(forms.Form):
    hoten = forms.CharField(label = 'hoten', max_length=200)
    masv = forms.CharField(label = 'masv', max_length=10)
    nganhhoc = forms.CharField(label = 'nganhhoc' ,max_length=20)

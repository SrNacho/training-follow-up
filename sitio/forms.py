from django import forms

class RegistroUsuarioForm(forms.Form):
  usuario = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Username'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class IngresoUsuarioForm(forms.Form):
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
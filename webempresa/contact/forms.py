from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput({'class':'form-control','placeholder':'Escríbe tu nombre', 'min_lenght':3, 'max_lenght':100}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput({'class':'form-control','placeholder':'Escríbe tu correo', 'min_lenght':3, 'max_lenght':100}))
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea({'class':'form-control','rows':3,'placeholder':'Escríbenos tu mensaje', 'min_lenght':10, 'max_lenght':1000}))

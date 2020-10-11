from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    file = forms.FileField()
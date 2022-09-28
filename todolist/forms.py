from django import forms

class addNewTask(forms.Form):
    Judul = forms.CharField(label='Title', required=True, max_length = 100)
    Deskripsi = forms.CharField(label='Description', required=True)
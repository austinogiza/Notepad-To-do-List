from django import forms


class TodoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'

    }))

    date = forms.DateField()

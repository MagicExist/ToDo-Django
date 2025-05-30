from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control w-50 mb-4'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control w-50 mb-4',
                                     'rows':4}),
        required=False
    )
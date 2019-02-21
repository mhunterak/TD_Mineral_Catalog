from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search',
            'style': 'width: 80%;',
            })
    )

from django import forms
from guestbookapp.models import Entry

class EntryForm (forms.ModelForm):

    user = forms.CharField (label = 'User', widget = forms.TextInput (attrs = {'size' : 32}))
    comment = forms.CharField (label = 'Your Comment', widget = forms.TextInput (attrs = {'size' : 64}))

    class Meta:
        model = Entry
        fields = ('user', 'comment', )
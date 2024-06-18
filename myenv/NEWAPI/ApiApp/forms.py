from django import forms
from.models import BookInfo

class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ('Title', 'Code', 'Linenous', 'Language', 'Style')
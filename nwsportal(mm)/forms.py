from django import forms
from .models import Post



class ClientDetailsForm(forms.ModelForm):
    date_of_birth = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
       model = Post

from django import forms
from select_image.models import ImgFiles

class PicForm(forms.ModelForm):
    class Meta:
        model = ImgFiles
        fields = ('name', 'image')

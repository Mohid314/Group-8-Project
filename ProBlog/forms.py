from django import forms
from .models import Post


class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Title'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
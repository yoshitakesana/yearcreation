from django import forms

from django.forms import ModelForm
from .models import Post


class ContactForm(forms.Form):
    name=forms.CharField(label='𝐍𝐚𝐦𝐞',max_length=30)
    email=forms.EmailField(label='𝐌𝐚𝐢𝐥')
    title=forms.CharField(label='𝐓𝐢𝐭𝐥𝐞',max_length=30)
    message=forms.CharField(label='𝐌𝐞𝐬𝐬𝐞𝐚𝐠𝐞',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder']='𝐏𝐥𝐞𝐚𝐬𝐞 𝐄𝐧𝐭𝐞𝐫'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='𝐏𝐥𝐞𝐚𝐬𝐞 𝐄𝐧𝐭𝐞𝐫'
        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['title'].widget.attrs['placeholder']='𝐏𝐥𝐞𝐚𝐬𝐞 𝐄𝐧𝐭𝐞𝐫'
        self.fields['message'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['placeholder']='𝐏𝐥𝐞𝐚𝐬𝐞 𝐄𝐧𝐭𝐞𝐫'

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['content','image1','image2']

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'コメントを書く...'})
        }

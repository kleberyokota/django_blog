from django import forms


from .models import Post

class PostNew(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['published_date', 'created_date']

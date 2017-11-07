from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = self.user
        post = super(PostForm, self).save(commit=False)
        post.user = user

        if commit:
            post.save()

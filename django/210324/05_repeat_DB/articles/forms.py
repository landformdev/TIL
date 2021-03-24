from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
    # title = forms.CharField()


# Model과 관련된 Form 클래스!
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
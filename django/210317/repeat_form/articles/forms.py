from django import forms
from .models import Article

# class ArticleForm(forms.Form):
    # title = forms.CharField()


# Model과 관련된 Form 클래스!
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
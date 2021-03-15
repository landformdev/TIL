from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시물 보여주는 페이지를 렌더하는 함수

    # articles = Article.objects.all()

    articles = Article.objects.order_by('-pk')

    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # pk에 해당하는 게시물 페이지를 랜더한다
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    # 새글 작성하는 템블릿을 랜더
    return render(request, 'articles/new.html')


def create(request):
    # 살제 DB에 게시물을 생성
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index') # urls 이름

def edit(request, pk):
    # 글을 수정하는 템플릿을 랜더하는 함수
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 실제 DB에 적용 (수정)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', pk)


def delete(request, pk):
    #실제 DB에 적용(삭제)
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
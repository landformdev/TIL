from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


#CREATE
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # request.GET.get('폼태그의 input태그 혹은 textarea태그의 name)(name이 key다.)
    title = request.GET.get('title')
    content = request.GET.get('content')

    # #1. 인스턴스 => 저장
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save() #=> return 이 없음!


    #2. 인스턴스 => 저장
    article = Article(title=title, content=content)
    article.save()

    # #3. 클래스 => 오브젝트 => 생성 = > return이 있다!
    # article = Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')

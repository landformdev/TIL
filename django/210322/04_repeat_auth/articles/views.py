from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    """
    모든 게시물을 보여주는 템플릿을 렌더하는 함수
    """
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    """
    게시물의 상세페이지를 렌더
    """
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    """
    GET: 새 글을 작성하는 템플릿을 랜더
    POST : DB에 새 글을 작성
    """

    if request.method == "POST":
        # 사용자로 부터 받은 정보(request.POST)가 담긴 인스턴스를 생성
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            article = form.save()  # 꼭 vaild 다음에 써야함
        
            return redirect('articles:detail', article.pk)

    else:
        # GET : form 클래스 사용!
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)



def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
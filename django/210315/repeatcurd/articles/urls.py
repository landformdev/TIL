from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    #~/articles/
    path('', views.index, name='index'),

    #~/articles/게시물번호 : 상세페이지를 랜더
    path('<int:pk>/', views.detail, name='detail'),

    #~/articles/new/ : 새글쓰는 템플릿을 랜더
    path('new/', views.new, name="new"),

    #~/articles/create/ : 실제 DB에 적용 (생성)
    path('create/', views.create, name='create'),

    #~/articles/게시물번호/edit/ : 글을 수정하는 템플릿을 랜더
    path('<int:pk>/edit', views.edit, name='edit'),

    #~/articles/게시물번호/update/ : 실제 DB에 적용 (수정)
    path('<int:pk>/update', views.update, name='update'),

    #~/articles/게시물번호/delete/ : 글을 삭제 (실제DB에 적용)
    path('<int:pk>/delete', views.delete, name='delete'),


]

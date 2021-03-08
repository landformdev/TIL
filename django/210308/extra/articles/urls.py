from django.urls import path
from . import views

urlpatterns = [
    #~/articles/로 접근하면 views의 index함수가 실행!
    path('', views.index),

    path('hello/', views.hello),

    #variable routing
    #~/articles/제목=>가변적/ 로 접근하면, views의 title 함수가 실행!
    path('<str:title>/<int:number>', views.title),

    path('throw/', views.throw),
    path('catch/', views.catch),
]

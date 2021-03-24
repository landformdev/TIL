from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# DB 유저 세션 생성(CREATE)
def login(request):
    """
    POST : 실제 로그인을 진행
    GET : 로그인 페이지 랜더
    """
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())

            # next 파라미터를 여기서 활용!
            # A or B
            # A : request.GET.get('next')가 존재한다면 B는 확인하지 않고  B 실행
            return redirect('articles:index')
    else:
        # form 인스턴스 : Form Class를 직접 만들지 않음!
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


# DB 유저 세션 삭제(DELETE)
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_logout(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form':form}

    return render(request, 'accounts/signup.html', context)


def create(request):
    if request.method == "POST":
        pass
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form':form}

    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:



#비밀번호 수정(UPDATE)
 
def change_password(request):
    if request.method == "POST":
        pass

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
        return render(request, 'accounts/update.html', context)

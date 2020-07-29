from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == "GET" :
        return render(request, 'main/main.html')

    elif request.method == "POST":
        login_ID = request.POST.get('email', None)
        login_password = request.POST.get('password', None)


        if not (login_ID and login_password):
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 모두 입력하세요.') # 첫번째, 초기지원
        else :
            try:
                myuser = User.objects.get(email=login_ID)
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
                if check_password(login_password, myuser.password):
                    request.session['user'] = myuser.email
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                    messages.add_message(request, messages.INFO, '로그인이 성공하였습니다')

                    return render(request, 'main/home.html')
                else:
                    messages.add_message(request, messages.INFO, '비밀번호가 틀렸습니다.') # 첫번째, 초기지원
            #아이디가 존재하지 않을 경우
            except User.DoesNotExist:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디입니다.') # 첫번째, 초기지원

        return render(request, 'main/main.html')

def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'main/signup.html')

    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        name = request.POST.get('name', None)   #딕셔너리형태
        # userimage = request

        if not (email and name and password and re_password) :
            messages.add_message(request, messages.INFO, '모든 값을 입력해야 합니다.!') # 첫번째, 초기지원
            return render(request, 'main/signup.html') #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            #return HttpResponse('비밀번호가 다릅니다.')
            messages.add_message(request, messages.INFO, '비밀번호가 다릅니다.') # 첫번째, 초기지원
            return render(request, 'main/signup.html') #register를 요청받으면 register.html 로 응답.

        else :
            user = User(email = email, password=make_password(password),name=name) #userimage도 받아야함
            user.save()
            messages.add_message(request, messages.INFO, '회원가입이 성공하였습니다')

            return redirect('/')

            #return render(request, 'home.html', res_data) #register를 요청받으면 register.html 로 응답.
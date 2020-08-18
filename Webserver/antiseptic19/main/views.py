from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
#JSON 요청을 위한 Parser 추가

from django.http import HttpResponse, JsonResponse
import simplejson
#CSRF TOKEN 무효
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
                    request.session['name'] = myuser.name
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                    messages.add_message(request, messages.INFO, '로그인이 성공하였습니다')

                    return redirect("/home")
                else:
                    messages.add_message(request, messages.INFO, '비밀번호가 틀렸습니다.') # 첫번째, 초기지원
            #아이디가 존재하지 않을 경우
            except User.DoesNotExist:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디입니다.') # 첫번째, 초기지원

        return render(request, 'main/main.html')

from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    res_data = {}
    info = {}
    if request.method == "GET":
        email = request.GET.get('email')
        if email:
            try:  # 아이디가 존재할 경우
                myuser = User.objects.get(email=email)
                request.session['idcheck'] = False
                overlap = "fail"
                info['overlap'] = overlap
            # 아이디가 존재하지 않을 경우
            except User.DoesNotExist:
                request.session['idcheck'] = True
                info['idcheck'] = email
                overlap = "pass"
                info['overlap'] = overlap
            return JsonResponse(info)
        else:
            return render(request, 'main/signup.html')

    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        name = request.POST.get('name', None)   #딕셔너리형태
        userimage = request.FILES['userimage']
        fs = FileSystemStorage()

        res_data['image_url'] = fs.url(userimage.name)
        if not (email and name and password and re_password and userimage) :
            messages.add_message(request, messages.INFO, '모든 값을 입력해야 합니다.!') # 첫번째, 초기지원
            return render(request, 'main/signup.html',res_data) #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            #return HttpResponse('비밀번호가 다릅니다.')
            messages.add_message(request, messages.INFO, '비밀번호가 다릅니다.') # 첫번째, 초기지원
            return render(request, 'main/signup.html',res_data) #register를 요청받으면 register.html 로 응답.

        else :
            user = User(email = email, password=make_password(password),name=name, userimage=userimage) #userimage도 받아야함
            user.save()
            messages.add_message(request, messages.INFO, '회원가입이 성공하였습니다')
            # return redirect("/")

            return render(request, 'main/success.html', res_data) #register를 요청받으면 register.



def home(request):
    return render(request, 'main/home.html')

def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
        del (request.session['name'])
    return redirect('/')

def mypage(request):
    list={}
    user_email=request.session.get('user')
    user_info = User.objects.get(email=user_email)
    list['user']=user_info
    return render(request,"main/mypage.html", list)

def dropout(request):
    del (request.session['user'])
    del (request.session['name'])

    return redirect('/')




#임시방편으로 CSRF 무효화 시킴.
@method_decorator(csrf_exempt,name='dispatch')
def app_signup(request):
    #앱 에서 오는 POST 요청
    if request.method == "GET":
        return render(request, 'main/app_signup.html')

    elif request.method == "POST":
        #data = JSONParser().parse(request)
        #serializer = PostSerializer(data=data)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        name = request.POST.get('name', None)
        #email = serializer['email']
        #password = serializer['password']
        #name=serializer['name']
        #사용자 정보를 사용자가 저장하기위해
        #여기서 Data  를 response 로 다시 보내줘야함
        
       
        user = User(email=email,password=make_password(password),name=name)
        user.save()
        
        return HttpResponse(simplejson.dumps({"email":email,"password":password,"name":name}))
#방 생성 통신 올때 난수코드를 바로 관리자에게 보여줘야함.
#POST 요청 -> data를 다시 response로 보내줌
#데이터 모델을 USER 외에 ROOM 을 하나 더 만듬.
#방 입장 통신 올때 난수코드를 비교해서 ROOM 입장
#ROOM 마다 상이하게 접속되는 url 만들기
#방 생성 혹은 입장시 사용자 정보를 관리자가 넣는것 x???
#방 입장부터는 socket.io 로 통신

@method_decorator(csrf_exempt,name='dispatch')
def app_login(request):
    #앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        #받은 이메일이랑 비밀번호 =데이터와 일치하면
        #리턴값으로 숫자 200 = 로그인 성공
        #일치 안하면 숫자 100 = 로그인 실패
        try:
            myuser = User.objects.get(email=email)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(password, myuser.password):
                request.session['user'] = myuser.email
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                

                return HttpResponse(200)
            else:
                return HttpResponse(100)
        #아이디가 존재하지 않을 경우
        except:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디입니다.') # 첫번째, 초기지원
   #아이디 삭제
    elif request.method=="DELETE":
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        User.objects.delete(email=email)

 
    

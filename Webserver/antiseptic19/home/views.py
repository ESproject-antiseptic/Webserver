from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from main.models import*
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def make_room(request): #방만들기
    info = {}
    if request.method == "GET":
        room_name = request.GET.get('room_name')
        if room_name:
            try: #룸이름이 중복되는 경우
                exist = Room.objects.get(room_name =room_name)
                overlap = "fail"
                info['overlap'] = overlap
            except Room.DoesNotExist:
                info['roomcheck']=room_name
                overlap="pass"
                info['orverlap']=overlap
            return JsonResponse(info)
        else:
            print('GET & else')
            return render(request, 'home/make_room.html')

    elif request.method == "POST":
        user_email = request.session.get('user')
        admin = User.objects.get(email=user_email)
        room_name = request.POST.get('room_name')
        room_ps=request.POST.get('room_ps')
        try:
            room_member =request.FILES['room_member'] #명단
        except :
            print('none')
            room_member= None
        check_values1=request.POST.getlist('chBox1') #명단 있어서 얼굴인식기능 선택
        print(check_values1)
        check_values=request.POST.getlist('chBox') #2.특정프로그램차단 3.WEB키보드 사용금지 4. APP 움직임 감지 5.마스크인식
        print(check_values)
        room_func = [] #기능들 번호 리스트
        if check_values1:#chBox1이면 'room_member'(명단)
            print('chbox1 존재')
            room_func.append('1')
            print(room_func)

        room_func.extend(check_values)
        print(room_func)

        if not (room_name and room_ps and room_func):
            messages.add_message(request, messages.INFO, '모든 값을 입력해야 합니다.!')  # 첫번째, 초기지원
            return render(request, 'home/make_room.html')
        else:
            info['admin']=admin
            info['room_name']=room_name
            info['room_ps']=room_ps
            room = Room(admin=admin, room_name=room_name, room_ps=room_ps, room_member=room_member,room_func=room_func)
            room.save()
            messages.add_message(request, messages.INFO, '방만들기가 성공하였습니다.')
        #fs = FileSystemStorage()
        # filename = fs.save(room_member.name, room_member)
        # uploaded_file_url=fs.url(filename)
        # print(uploaded_file_url)

            return render(request, 'home/make_room_success.html',info) #성공

#방들어가기
def enter_room(request):
    return render(request,'home/enter_room.html')

def myroom(request):
    return render(request, 'home/myroom.html')

def myroom1(request):
    user_email=request.session.get('user')
    admin = User.objects.get(email=user_email)
    room = Room.objects.filter(admin=admin)
    rooms= room.order_by('-id')
    return render(request, 'home/myroom1.html', {"rooms":rooms})





#우림이 test해보기
def test(request):
    return render(request, 'home/test.html')


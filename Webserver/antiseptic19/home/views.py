from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

#방만들기
def make_room(request):
    return render(request, 'home/make_room.html')

#방들어가기
def enter_room(request):
    return render(request,'home/enter_room.html')

#우림이 test해보기
def test(request):
    return render(request, 'home/test.html')

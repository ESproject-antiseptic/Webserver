from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dface import opencv_dface
from .opencv_dface1 import opencv_dface1
import numpy as np
import cv2

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
    if request.method =='POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'home/test.html',{'form':form,'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'home/test.html',{'form':form})

def test1(request):
    return render(request, 'home/test1.html',)

def cam(request):
    '''imageURL = settings.MEDIA_URL
    opencv_dface1(settings.MEDIA_ROOT_URL + imageURL)'''
    return render(request, 'home/cam.html')

def index(request):
    return render(request, 'home/index.html',)




'''def capture_video_from_cam():
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    while True:

        ret, frame = cap.read()

        # Handles the mirroring of the current frame
        frame = cv2.flip(frame,1)
        currentFrame += 1'''
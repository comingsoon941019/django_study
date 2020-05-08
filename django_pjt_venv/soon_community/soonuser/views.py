from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import soonuser

# Create your views here.

def home(request):
  user_id = request.session.get('user')

  if user_id:
    soonuser1 = soonuser.objects.get(pk=user_id)
    return HttpResponse(soonuser1.username)

  return HttpResponse('Home')

def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  elif request.method == "POST":
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)

    res_data = {}
    if not (username and password):
      res_data['error'] = 'ID와 비밀번호를 입력하여 주세요.'
    else:
      soonuser1 = soonuser.objects.get(username=username)
      if check_password(password, soonuser1.password):
        request.session['user'] = soonuser1.id
        return redirect('/')
      else:
        res_data['error']='비밀번호를 틀렸습니다.'
    
    return render(request,'login.html',res_data)


def register(request):
  if request.method == "GET":
    return render(request, 'register.html')
  elif request.method == "POST":
    username = request.POST.get('username',None)
    useremail = request.POST.get('useremail',None)
    password = request.POST.get('password',None)
    re_password = request.POST.get('re-password',None)

    res_data = {}
    if not (username and useremail and password and re_password): 
      res_data['error']="모든 값을 입력해야 합니다."
    elif password != re_password:
      res_data['error']="비밀번호가 다릅니다."
    else:
      user = soonuser(
       username = username,
       useremail = useremail,
       password = make_password(password)
      )
      user.save()

    return render(request, 'register.html', res_data)
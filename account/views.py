from django.shortcuts import render,redirect
from django.contrib.auth.models import User # 계정 생성과 로그인 기능을 구현할 때 사용. django 자체에 내장되어 있는 user 모델 불러오기. 
from django.contrib import auth # 사용할 user 모델이 auth안에 있으니까 auth도 불러오기.

# Create your views here.
def signup(request):
    if request.method == 'POST': # POST는 데이터가 전송되는 방식 중 하나로 데이터가 눈에 보이지 않는 방식으로 전달됨. (RESTful - HTTP method 찾아보기)
        if request.POST['password1'] == request.POST['password2']:
            #try:
                #user = User.objcets.get(username = request.POST['username'])
                #return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            #except User.DoesNotExit:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                # User 클래스를 기반으로 한 쿼리셋에서 유저를 만드는 함수라고 하네요..
                auth.login(request, user) # 회원 가입이 끝나면 바로 로그인이 되도록 하는 함수..
                return redirect('home') # redirect를 쓰려면 미리 선언해야 함. home이라는 이름을 가진 url로 이동하라는 의미. 
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords must match'})
    return render(request, 'account/signup.html') # templates 폴더 안에 있는 account 폴더 안에 있는 signup.html(template)을 불러오라는 의미.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        # 데이터베이스에서 전달받은 username과 password를 가지고 사용자가 존재하는지 판단!!! 
        
        if user is not None: # 예외처리를 해주는 부분
            auth.login(request, user) # user 정보가 있으면 로그인
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error':'username or password is incorrect'}) 
            # user 정보가 없으면, login.html를 반환하고 에러 메시지를 띄움.
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'account/signup.html')

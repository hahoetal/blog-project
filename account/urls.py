from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
]

# 사용자 계정과 관련된 url만 모아놓은 python 파일
# project 폴더(setting.py가 있는..)에 있는 urls.py에 작성해도 되지만, 코드가 길어지는 것을 방지하기 손쉽게 관리하기 위해 따로 만들기도 함.
# 이를 사용할 경우, project 폴더의 urls.py에 들어가서 'from django.urls import path' 옆에 'include'를 쓰고
# urlpatterns 안에 path('app 이름/', include('app 이름.urls')) 이런 식으로 작성해야 함.
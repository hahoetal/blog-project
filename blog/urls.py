from django.contrib import admin
from django.urls import path
from . import views # 같은 폴더에 있는 views.py의 내용을 가져와라! 안 하면 오류남.

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newblog/', views.blogpost, name ="newblog"),
    path('search', views.search, name="search"),
    path('<int:blog_id>/postremove', views.postremove, name="postremove"),
    path('<int:blog_id>/postedit', views.postedit, name="postedit"),
]

# <int:blog_id>에는 각 게시물의 id 값이 들어가게 됨.
# 이런 것을 path-converter라고 함. 
# 장고에서 여러 객체들을 다루는 계층적 url이 필요할 때 사용하고 <type:name>와 같은 모양.
# 지정한 converter type의 name 변수를 view 함수로 넘기라는 의미..
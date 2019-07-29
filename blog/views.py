from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone # 자동적으로 서버의 시간을 입력해주고 싶을 때 사용.
from django.core.paginator import Paginator # 객체가 한 페이지에 전부 출력되지 않게 하고 싶을 때 사용!
from .models import Blog # 모델을 쓰고 싶으면 가져오기.
from .form import BlogPost # 장고 폼을 쓰고 싶으면 가져오기.

# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all() # 일단 블로그 객체를 전부 가져오고
    paginator = Paginator(blog_list,3) #Paginator를 이용해서 블로그 객체들을 3개씩 분할. 한 페이지에 3개씩.
    page = request.GET.get('page') # request된 페이지를 알아내서 'page(변수 임)'에 담음
    posts = paginator.get_page(page) # request된 페이지를 얻어와서 담음.
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # get_object_or_404 객체가 있으면 가져오고, 없으면 404 오류를 내라... 클래스명과 pk값으로 가져올 데이터 구분.
    # pk는 primary key의 약어. 모델에서 찍어낸 수많은 객체를 구분하는 구분자.
    # id는 장고가 알아서 만들어줌.
    return render(request, 'detail.html',{'blogs':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() # Blog 클래스를 가져오고
    blog.title = request.GET['title'] # title이라는 이름을 가진 <input>에 입력한 내용은 blog.title에 담아.
    blog.body = request.GET['body'] # body라는 이름을 가진 <input>에 입력한 내용은 blog.body에 담아.
    blog.pub_date = timezone.datetime.now() # timezone에서 현재 시각과 날짜를 받아 와!
    blog.save() # 저장!!
    return redirect('/blog/' +str(blog.id)) # /blog/에 blog_id를 붙인 것과 똑같은 url로 이동.

def blogpost(request): #장고 폼을 이용해서 글을 작성하는 함수
    #입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            # BlogPost form에서 제목과 본문만 입력받기 때문에 날짜와 시간은 views 함수 내에서 넣어주어야 함.
            # 그래서 아직은 사용자가 입력한 내용은 저장하지 말고, 모델 객체를 반환하라는 의미.
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    #빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new1.html', {'form': form})

def search(request): # 검색 기능 담당 함수.
    try: # 일단 시도하고
        type_search = request.GET.get('selSearchType')
        txt_search = request.GET.get('txtSearch')
        if type_search == "전체":
            search_list = Blog.objects.filter(title__contains=txt_search)
            search_list = Blog.objects.filter(body__contains=txt_search)
        elif type_search == "제목":    
            search_list = Blog.objects.filter(title__contains=txt_search) # 블로그 객체들 중 title에 "txt_search(사용자가 입력한 것)" 포함된 객체만 담아.
        else :
            search_list = Blog.objects.filter(body__contains=txt_search) # 블로그 객체들 중 body에 "txt_search(사용자가 입력한 것)" 포함된 객체만 담아.
    except: # 안 되면 이걸 시행해.
        blog_lists = Blog.objects.all()
    return render(request, 'search.html', {'search_list': search_list})

def postremove(request, blog_id): # 게시글을 삭제하는 함수.
    blog = Blog.objects.get(pk = blog_id)
    blog.delete()
    return redirect('home')
    
def postedit(request, blog_id): # 게시글을 수정하는 함수(html 폼을 이용).
    post = get_object_or_404(Blog, id=blog_id) # 수정하려는 게시글을 받아오고

    if request.method == "POST": # POST 방식으로 데이터를 입력받으면
        title = request.POST.get('title') # 해당되는 정보를 입력받아 변수에 담고
        body = request.POST.get('body')
        post.title = title # 그것을 가져온 게시글의 해당하는 곳에 넣어줍니다.
        post.body = body
        post.save() # 저장
        return redirect('detail', post.pk)
    return render(request, 'edit.html', {'post':post}) # 수정하려는 게시글을 가져와서 edit.html에 담아줌.
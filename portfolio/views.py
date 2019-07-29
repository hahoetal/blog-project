from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Portfolio
from .form import PortfolioPost
from django.http import HttpResponseRedirect # 이미지를 저장한 뒤에 이미지와 제목, 설명이 나오는 페이지가 나오도록 하기 위해 쓴 코드가 있는데 이를 쓰려면 불러와야 함.
                                             # 정확히 뭔지는 몰라서 나중에 한 번 찾아보기.

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios':portfolios})

def show(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id) # 모델에서 찍어낸 객체들을 구분해주는 구분자(pk,primary key)로써 portfolio_id를 사용.
    return render(request, 'portfolio/show.html', {'portfolios':portfolio_detail})

def newimage(request): 
        # 입력된 내용을 처리.
    if request.method == 'POST':
        form = PortfolioPost(request.POST, request.FILES) # 사용자가 입력한 내용, 업로드한 사진(파일)이 form.py에서 정의한대로 담겨있는 것을 form에 넣기.
        if form.is_valid(): # form에 있는 내용이 유효한 경우,
            portfolios = form.save(commit=False) # 아직 저장하지 말고
            portfolios.pub_date = timezone.datetime.now() # 서버로 부터 시간을 받아와서
            portfolios.save() # 저장
            return HttpResponseRedirect('/portfolio/')
        # 아직 내용을 입력하지 않은 경우, 사용자가 이미지와 글을 입력할 수 있는 폼을 출력.
    else:
        form = PortfolioPost() # 개발자가 정의한 PortfolioPost 클래스 불러오기.
        return render(request, 'portfolio/image.html', {'form': form})

def remove(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk = portfolio_id)
    portfolio.delete() # 삭제.
    return redirect('portfolio')

def edit(request, portfolio_id):
    portfolios = Portfolio.objects.get(id =portfolio_id)

    if request.method =="POST":
        forms = PortfolioPost(request.POST, request.FILES)
        if forms.is_valid():
            print(form.cleaned_data)
            portfolios.title = form.cleaned_data['title']
            portfolios.image = form.cleaned_data['image']
            portfolios.description = form.cleaned_data['description']
            portfolios.save()
            return redirect('/portfolio/'+str(portfolios.pk))
    else:
        forms = PortfolioPost(instance=portfolios)
        return render(request, 'portfolio/edits.html', {'forms':forms})
# 고칠 필요가 있는 코드.
# 기존의 내용이 담겨오지만... 게시물을 새로 작성하는 것과 마찬가지임. 제목, 이미지, 사진 설명을 모두 수정해야만 오류 메시지가 뜨지 않음. 
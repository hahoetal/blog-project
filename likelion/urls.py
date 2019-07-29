"""likelion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings # 이것도 추가(나중에 알아보기, 일단 static의 media를 쓰려고 추가했구나 정도로 알기. 왜냐면 이거 할 때 추가했으니까.)
from django.conf.urls.static import static # static을 이용하기 위해 추가.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 사용자가 올린 파일을 읽어올 수 있도록 추가(나중에 더 자세히 알아보기).

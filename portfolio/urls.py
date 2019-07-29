from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('<int:portfolio_id>', views.show, name="portfolios"),
    path('image/', views.newimage, name="newimage"),
    path('<int:portfolio_id>/remove', views.remove, name="remove"),
    path('<int:portfolio_id>/edit', views.edit, name="edit"),
]

# <int:portfolio_id>, path-converter
# 여러 객체를 다루는 계층적 url이 필요할 때 사용함.
from django.contrib import admin
from .models import Portfolio # Portfolio가 뭔지 모를테니 models.py에 있는 것 불러오기.

# Register your models here.
admin.site.register(Portfolio) # portfolio DB를 사용한다고 알리기.
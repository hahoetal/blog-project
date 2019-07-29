from django.contrib import admin
from .models import Blog # 같은 파일에 있는 model.py에서 Blog를 가져 와라.
# Register your models here.

admin.site.register(Blog) # admin site에 Blog를 가져다 놓겠다?? 이거 안 하면 admin site에 Blog가 안 보이고, 데이터 추가와 수정이 불가능.

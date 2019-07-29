from django.db import models

# Create your models here.
class Blog(models.Model): # 클래스를 이용해서 새로운 데이터형을 만들어줌.
    title = models.CharField(max_length=200, null = False)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null = False)

    def __str__(self): # 게시글의 제목이 반환됨...
        return self.title

    def summary(self):
        return self.body[:100] # body에 들어간 내용 중 100글자만 반환.
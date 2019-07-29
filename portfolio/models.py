from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length =255)
    image = models.ImageField(upload_to = 'images/') # 업로드된 이미지를 image 폴더에 넣어라. 
    description = models.TextField(max_length = 500)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:60]
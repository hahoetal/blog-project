# django form을 사용하기 위해 만든 python 파일.
# html 파일을 만들지 않아도 되고, 데이터의 유효성 검증이 가능해서 편리함.

from django import forms # django에서 제공하는 form을 사용할 것이니까 불러오기.
from .models import Blog # models.py에 만들어둔 Blog를 이용할 것이니까 불어오기.

class BlogPost(forms.ModelForm): # 모델을 기반으로 하는 클래스를 만들기 때문에 인자로 ModelForm을 넘겨줌.
    class Meta: # 어... 뭔가 엄청 어려운데... 이미 만들어진 클래스를 가지고 새로운 클래스를 만들기 때문에 사용하는 듯하다.
        model = Blog # 사용할 모델의 이름.
        fields = ['title', 'body'] # Blog에서 사용할 것들은 []안에 입력. 그럼 자동으로 입력란이 만들어짐.

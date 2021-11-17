from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class User(AbstractUser):
#     user_id = models.CharField(max_length=15)


class User(models.Model):
    # 회원가입하는 ID
    user_id = models.CharField(db_column='id', primary_key=True, max_length = 15)
    # password
    password = models.CharField(max_length = 20)
    # 이름
    name  = models.CharField(max_length = 20)
    # 성별
    gender  = models.CharField(max_length = 2)
    # 키
    height  = models.CharField(max_length = 20)
    # 체중
    weight  = models.CharField(max_length = 20)
    # 연령
    age  = models.CharField(max_length = 20)
    # 활동량
    activity  = models.CharField(max_length = 20)    
    # id 생성일자
    created_dt = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self): # 이 함수 추가
        return self.user_id  # User object 대신 나타낼 문자
    
class Meta: #메타 클래스를 이용하여 테이블명 지정
    db_table = 'project.user_info'
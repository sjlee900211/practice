from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) #foreignkey 설정(카테고리를 삭제하면 기본 카테고리로 설정)
    restaurant_name = models.CharField(max_length = 100) #맛집 이름
    restaurant_link = models.CharField(max_length = 500) #맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length = 50) #키워드


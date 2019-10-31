from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250) #컬럼속성 및 제약조건
    author = models.CharField(max_length=50)
    content = models.TextField(blank=True) 
    view_count = models.IntegerField(default=0) #정수데이터 저장 필드, default 를 쓰면 0값으로 null 을 채워줌.
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


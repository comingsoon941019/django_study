from django.db import models

# Create your models here.
class soonuser(models.Model): #models.Model을 상속 받아야함
  username = models.CharField(max_length=64, verbose_name='사용자명') #verbose_name = 확인 필요
  useremail = models.EmailField(max_length=128, verbose_name="사용자 이메일")
  password = models.CharField(max_length=64, verbose_name='비밀번호')
  registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  def __str__(self):
    return self.username
   
  class Meta: 
    db_table = 'fastcampus_user'
    verbose_name = "패캠 사용자" 
    verbose_name_plural = "패캠 사용자"

 
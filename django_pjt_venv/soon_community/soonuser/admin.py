from django.contrib import admin
from .models import soonuser
# Register your models here.


class soonuserAdmin(admin.ModelAdmin):
 list_display = ('username','useremail','password') #클래스 안의 필드 표시

admin.site.register(soonuser,soonuserAdmin) #??


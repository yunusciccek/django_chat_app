from django.contrib.auth.models import User
from django.db import models
import uuid

class Room(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='firstuser', verbose_name='ilk kullanıcı', blank=True, null=True)
    second_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='seconduser',verbose_name='ikinci kullanıcı',blank=True,null=True)

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='messages',verbose_name='kullanıcı')
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='messages',verbose_name='oda')
    content = models.TextField(verbose_name='mesaj içeriği')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='oluşturulma tarihi')
    
    def get_short_date(self):
        return str(self.created_date.hour) + ":" + str(self.created_date.minute)
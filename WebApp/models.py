from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class user(models.Model):
    gym_user_id     = models.AutoField(primary_key=True)
    user_Name       = models.CharField(max_length=100, default=None, blank=True, null=True)
    password        = models.CharField(max_length=100, default=None, blank=True, null=True)
    email           = models.EmailField(max_length=100, default=None, blank=True, null=True)
    account_status 	= models.BooleanField(default=True)
    last_login_time	= models.DateTimeField(auto_now=True)
    contact_no      = models.IntegerField( default=None, blank=True, null=True)
    new_id       = models.ForeignKey(User, to_field='id',   related_name="user_id_list" ,  on_delete=models.CASCADE)

    def __str__(self):
        #return self.User.username,self.account_status
        return '{} {}  '.format(self.user_Name,self.account_status)
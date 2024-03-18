from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# class Region(models.Model):
#     region_id      = models.AutoField(primary_key=True)
#     region_txt     = models.CharField(max_length=200, default=None, blank=True, null=True)
#     region_code    = models.CharField(max_length=10, default=None, blank=True, null=True)
#     region_status  = models.IntegerField(default=None, blank=True, null=True)
#     def __str__(self):
#         #return self.region_txt,self.region_code,self.region_id
#         #return '%s %s'%(self.region_txt,self.region_code)
#         return '{} {} {} '.format(self.region_txt,self.region_code,self.region_id)

# class Depot(models.Model):
#     depot_id              = models.AutoField(primary_key=True)
#     depot_txt             = models.CharField(max_length=100, default=None, blank=True, null=True)
#     deport_tel            = models.CharField(max_length=100, default=None, blank=True, null=True)
#     deport_code           = models.CharField(max_length=100, default=None, blank=True, null=True)
#     deport_image_location = models.CharField(max_length=500, default=None, blank=True, null=True)
#     priority              = models.BooleanField(default=True)
#     sortid                = models.BooleanField(default=True)
#     depo_location         =models.CharField(max_length=100, default=None, blank=True, null=True)
#     region_id             = models.ForeignKey(Region, to_field='region_id', related_name="users_region_set" , on_delete=models.CASCADE)

#     def __str__(self):
#         #return self.depot_txt
#         return '{} {}  '.format(self.depot_txt,self.deport_code)

# class UserLevel(models.Model):
#     level_id              = models.AutoField(primary_key=True)
#     level_name            = models.CharField(max_length=100, default=None, blank=True, null=True)
#     avalableUserLevel     = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.level_name

# class User(models.Model):
#     Gym_User            = models.OneToOneField(User, on_delete=models.CASCADE)
#     # gym_user_id    = models.AutoField(primary_key=True)
#     account_status 	= models.BooleanField(default=True)
#     last_login_time	= models.DateTimeField(auto_now=True) 
#     contact_no      = models.IntegerField( default=None, blank=True, null=True)
#     # region_id       = models.ForeignKey(Region, to_field='region_id',   related_name="region_id_list" ,  on_delete=models.CASCADE) 
#     # depot_id        = models.ForeignKey(Depot,  to_field='depot_id',    related_name="deport_id_list" ,  on_delete=models.CASCADE) 
#     # level_id        = models.ForeignKey(UserLevel, to_field='level_id', related_name="users_level_list", on_delete=models.CASCADE) 

#     def __str__(self):
#         #return self.User.username,self.account_status
#         return '{} {}  '.format(self.Gym_User,self.account_status)


class user(models.Model):
    gym_user_id     = models.AutoField(primary_key=True)
    user_Name       = models.CharField(max_length=100, default=None, blank=True, null=True)
    password        = models.CharField(max_length=100, default=None, blank=True, null=True)
    email           = models.EmailField(max_length=100, default=None, blank=True, null=True)
    account_status 	= models.BooleanField(default=True)
    last_login_time	= models.DateTimeField(auto_now=True) 
    contact_no      = models.IntegerField( default=None, blank=True, null=True)
    new_id       = models.ForeignKey(User, to_field='id',   related_name="user_id_list" ,  on_delete=models.CASCADE) 
    # depot_id        = models.ForeignKey(Depot,  to_field='depot_id',    related_name="deport_id_list" ,  on_delete=models.CASCADE) 
    # level_id        = models.ForeignKey(UserLevel, to_field='level_id', related_name="users_level_list", on_delete=models.CASCADE) 

    def __str__(self):
        #return self.User.username,self.account_status
        return '{} {}  '.format(self.user_Name,self.account_status)
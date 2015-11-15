from django.db import models

class user_details(models.Model):
    User_ID = models.CharField(max_length=8,  primary_key=True, default="DMS_0000")
    User_Name = models.CharField(max_length=20, null=True, blank=True, unique=True)
    Name = models.CharField(max_length=20, null=True, blank=True)
    USN = models.CharField(max_length=10, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Mobile_Number = models.CharField(max_length=10, null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Password = models.CharField(max_length=16, null=True, blank=True)
   
    def __unicode__(self):
        return u'%s -- %s' % (self.User_ID, self.User_Name)

    class Meta:
        managed = True
        db_table = "user_details"
        ordering = ['pk']
        verbose_name_plural = "user_details"
        
class user_login(models.Model):
    User_ID = models.ForeignKey(user_details, to_field='User_ID', related_name="User_ID_Loggedin", db_column="User_ID")
    Logged_In_Time = models.DateTimeField(null=True, blank=True)
    Logged_Out_Time = models.DateTimeField(null=True, blank=True)
    Status = models.CharField(max_length=10, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.User_ID)
    
    class Meta:
        managed = True
        db_table = "user_login"
        
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
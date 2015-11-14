from django.db import models
from login.models import user_details
 
class advertisement(models.Model):
    Advertisement_ID = models.CharField(max_length=8, primary_key=True, default="ADV_0000")
    Title = models.CharField(max_length=100, null=True, blank=True)
    Post_Date = models.DateTimeField(null=True, blank=True)
    Sold_Date = models.DateTimeField(null=True, blank=True)
    Status = models.CharField(max_length=10, null=True, blank=True)
    Seller_User_ID = models.ForeignKey(user_details, to_field='User_ID', related_name="Seller_User_ID")
    Buyer_User_ID = models.ForeignKey(user_details, to_field='User_ID', related_name="Buyer_User_ID")
    MRP = models.IntegerField(null=True, blank=True)
    Selling_Price = models.IntegerField(null=True, blank=True)
    Image1 = models.TextField(null=True, blank=True)
    Advertisement_Tag1 = models.CharField(max_length=50, null=True, blank=True)
    Advertisement_Tag2 = models.CharField(max_length=50, null=True, blank=True)
    Advertisement_Tag3 = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
 
    def __unicode__(self):
        return u'%s -- %s' % (self.Advertisement_ID, self.Title)
     
    class meta:
        managed = True
        db_table = "advertisement"
        ordering = ['pk']
 
 
class category(models.Model):
    Advertisement_ID = models.ForeignKey(advertisement, to_field='Advertisement_ID')
    Product_ID = models.CharField(max_length=8, primary_key=True, default="PRD_0000")
    Category = models.CharField(max_length=16, null=True, blank=True)
      
    def __unicode__(self):
        return u'%s -- %s' % (self.Product_ID, self.Advertisement_ID)
     
    class meta:
        managed = True
        db_table = "category"
        ordering = ['pk']
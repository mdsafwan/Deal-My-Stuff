from django.db import models
from login.models import user_details
 
class advertisement(models.Model):
    Advertisement_ID = models.CharField(max_length=8, primary_key=True, default="ADV_0000")
    Title = models.CharField(max_length=100, null=True, blank=True)
    Post_Date = models.DateTimeField(null=True, blank=True)
    Sold_Date = models.DateTimeField(null=True, blank=True)
    Status = models.CharField(max_length=10, null=True, blank=True)
    Seller_User_ID = models.ForeignKey(user_details, to_field='User_ID', related_name="Seller_User_ID", db_column='Seller_User_ID')
    Buyer_User_ID = models.ForeignKey(user_details, to_field='User_ID', related_name="Buyer_User_ID", db_column='Buyer_User_ID')
    MRP = models.IntegerField(null=True, blank=True)
    Selling_Price = models.IntegerField(null=True, blank=True)
    Image1 = models.TextField(null=True, blank=True)
    Advertisement_Tag1 = models.CharField(max_length=50, null=True, blank=True)
    Advertisement_Tag2 = models.CharField(max_length=50, null=True, blank=True)
    Advertisement_Tag3 = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
 
    def __unicode__(self):
        return u'%s -- %s' % (self.Advertisement_ID, self.Title)
     
    class Meta:
        managed = True
        db_table = "advertisement"
        ordering = ['pk']
        verbose_name_plural = "advertisements"
 
class category(models.Model):
    Advertisement_ID = models.ForeignKey(advertisement, to_field='Advertisement_ID', db_column='Advertisement_ID')
    Product_ID = models.CharField(max_length=8, primary_key=True, default="PRD_0000")
    Category = models.CharField(max_length=16, null=True, blank=True)
      
    def __unicode__(self):
        return u'%s -- %s' % (self.Product_ID, self.Advertisement_ID)
     
    class Meta:
        managed = True
        db_table = "category"
        ordering = ['pk']
        verbose_name_plural = "categories"
        
class electronic_gadget(models.Model):
    Product_ID = models.ForeignKey(category, to_field="Product_ID", db_column="Product_ID")
    Brand = models.CharField(max_length=100, null=True, blank=True)
    Product_Model = models.CharField(max_length=100, null=True, blank=True)
    Specification = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.Product_ID)
    
    class Meta:
        db_table = "electronic_gadget"
        verbose_name_plural = "electronic_gadgets"
        
class book(models.Model):
    Product_ID = models.ForeignKey(category, to_field="Product_ID", db_column="Product_ID")
    Genre = models.CharField(max_length=100, null=True, blank=True)
    Book_Language = models.CharField(max_length=100, null=True, blank=True)
    Publisher = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.Product_ID)
    
    class Meta:
        db_table = "book"
        verbose_name_plural = "books"
        
class vehicle(models.Model):
    Product_ID = models.ForeignKey(category, to_field="Product_ID", db_column="Product_ID")
    Manufacturer = models.CharField(max_length=100, null=True, blank=True)
    Product_Model = models.CharField(max_length=100, null=True, blank=True)
    Year = models.CharField(max_length=4, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.Product_ID)
    
    class Meta:
        db_table = "vehicle"
        verbose_name_plural = "vehicles"
        
class household_item(models.Model):
    Product_ID = models.ForeignKey(category, to_field="Product_ID", db_column="Product_ID")
    Brand = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.Product_ID)
    
    class Meta:
        db_table = "household_item"
        verbose_name_plural = "household_items"
        
from pickle import TRUE
from django.db import models
from django.contrib.gis.db import models as gis_models



class farm(models.Model):
    grower_id = models.IntegerField(unique=True,null=True)
    area = models.IntegerField(null=True)
    geom = gis_models.MultiPolygonField()

    class Meta:
        db_table = 'farms'
        verbose_name =('Farm')
        verbose_name_plural = ('Farms') 
    
    def __str__(self):
        """Return string representation."""
        return self.grower_id

class farmer(models.Model):
    email = models.EmailField( max_length=254, unique=True, db_index=True,default = 'fname.last@email.com', verbose_name= ("Email") )
    farmID = models.ForeignKey(farm, verbose_name=("Grower ID"), on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, default='First')
    lname = models.CharField(max_length=50, default='Last')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    income = models.IntegerField()


    class Meta:
        db_table = 'farmer'
        verbose_name =('Farmer')
        verbose_name_plural = ('Farmers')     

    def __str__(self):
        return self.fname

class partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='main.partner.logo', height_field=None, width_field=None, max_length=None)
    contact = models.EmailField(max_length=254)
    web = models.URLField(max_length=200)
    
    class Meta:
        db_table = 'partners'
        verbose_name =('Partner')
        verbose_name_plural = ('Partners')      

    def __str__(self):
        return self.name

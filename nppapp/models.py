from django.db import models

# Create your models here.
class postindtable(models.Model):
	officename=models.CharField(max_length=50)
	pincode = models.CharField(max_length=50)
	officeType = models.CharField(max_length = 100)
	Deliverystatus = models.CharField(max_length = 100)
	divisionname = models.CharField(max_length = 100)
	regionname = models.CharField(max_length = 100)
	circlename = models.CharField(max_length = 100)
	taluk = models.CharField(max_length = 100)
	Districtname = models.CharField(max_length = 100)
	statename = models.CharField(max_length = 100)

#def __unicode__(self):
	#return "%s, %s %s %s %s %s %s " % (self.city, self.statecode, self.zipcode)



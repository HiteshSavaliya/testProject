from django.db import models

class Employee (models.Model):
	def __unicode__(self):
		return self.name;
	name = models.CharField(max_length=256)
	empId = models.CharField(max_length=256)
	startDate = models.DateTimeField('start Date')

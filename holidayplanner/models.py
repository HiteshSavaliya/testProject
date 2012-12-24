from django.db import models

class Employee (models.Model):
	name = models.CharField(max_length=256)
	empId = models.CharField(max_length=256)
	startDate = models.DateTimeField('start Date')

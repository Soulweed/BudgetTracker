from django.db import models
from datetime import datetime
# Create your models here.
class Income(models.Model):
    def number():
        no = Income.objects.count()
        return no + 1
    
    tid = models.IntegerField(primary_key=True,unique=True,default=number)
    income_type = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    amount = models.FloatField(blank=False, null=False)
    recurring = models.BooleanField()
    ondate = models.TextField()
    recurr = models.TextField(default='0')
    date_recurr = models.DateTimeField(default= datetime.now, blank=True)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def __unicode__(self):
        
        pass
    
class Expense(models.Model):
    def number():
        no = Expense.objects.count()
        return no + 1
    
    tid = models.IntegerField(primary_key=True,unique=True,default=number)
    expense_type = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        
        pass

